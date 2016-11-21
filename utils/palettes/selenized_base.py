from __future__ import division

ACCENTS_MAX_REASONABLE_L = 75

def generate_palette(
    background,
    foreground,
    saturation=1,
    accent_offset=0,
    br_accent_shift=None,
    br_bg_extra_saturation=1.2
):
    bg_l, bg_a, bg_b = background
    fg_l, fg_a, fg_b = foreground

    # lightness relationships of many colors are expressed in terms of overall
    # palette contrast
    contrast = abs(fg_l - bg_l)

    # for palettes that have dark text on light background we invert lightness
    # changes (i.e. "bright" colors are darker)
    direction = -1 if bg_l > fg_l else 1



    ### MONOTONES

    # bright bg and fg are calculated using contrast. For some reason bright
    # background looks washed out without increased saturation
    br_bg_l = bg_l + direction*contrast/7
    br_bg_a, br_bg_b = bg_a*br_bg_extra_saturation, bg_b*br_bg_extra_saturation

    hi_bg_l = bg_l + direction*contrast/3

    br_fg_l = fg_l + direction*contrast/5

    # color used for comments and other secondary content; it's a weighted
    # average of fg and bg
    dim_fg_l = 1/3 * bg_l + 2/3 * fg_l
    dim_fg_a = 1/3 * bg_a + 2/3 * fg_a
    dim_fg_b = 1/3 * bg_b + 2/3 * fg_b

    monotones = {
        "bg":       [bg_l,     bg_a,     bg_b    ],
        "black":    [br_bg_l,  br_bg_a,  br_bg_b ],
        "br_black": [hi_bg_l,  br_bg_a,  br_bg_b ],
        "fg":       [fg_l,     fg_a,     fg_b    ],
        "white":    [dim_fg_l, dim_fg_a, dim_fg_b],
        "br_white": [br_fg_l,  fg_a,     fg_b    ],
    }



    ### ACCENTS

    # accents should have lightness close to foreground, except when foreground
    # is very bright (very bright accents look washed out)
    accent_base_l = min(
        fg_l,
        ACCENTS_MAX_REASONABLE_L + 0.5 * (fg_l-ACCENTS_MAX_REASONABLE_L)
    )
    # optionally move accent colors further away from foreground
    accent_base_l -= direction*accent_offset

    # accent colors lightness shouldn't be exactly uniform, but on the other
    # hand they shouldn't be too far away from each other.
    accent_l_spread = abs(accent_base_l - bg_l)/3

    # in dark-on-light palettes it's the darkest accents that should have
    # lightness close to foreground
    if direction == -1:
        accent_base_l += accent_l_spread

    accents = {
        "red":      [accent_base_l - 0.84*accent_l_spread,  63,  40],
        "orange":   [accent_base_l - 0.48*accent_l_spread,  37,  50],
        "yellow":   [accent_base_l - 0.06*accent_l_spread,   6,  65],
        "green":    [accent_base_l - 0.36*accent_l_spread, -37,  53],
        "cyan":     [accent_base_l - 0.12*accent_l_spread, -40,  -4],
        "blue":     [accent_base_l - 0.84*accent_l_spread,   0, -55],
        "violet":   [accent_base_l - 0.66*accent_l_spread,  33, -48],
        "magenta":  [accent_base_l - 0.60*accent_l_spread,  59, -21],
    }

    # bright accents have the same a* b* coords as regular accents and
    # uniformly shifted lightness
    if not br_accent_shift:
        br_accent_shift = contrast/10

    br_accents = {
        'br_'+name: [l + direction*br_accent_shift, a, b]
        for name, [l, a, b]
        in accents.iteritems()
    }



    ### FINAL ASSEMBLY

    # some debug
    print "Foreground:", fg_l
    print "Background:", bg_l
    print "Contrast:", contrast
    print "Accents max lightness:", accent_base_l
    print "Accents min lightness: {:.3}".format(accent_base_l - accent_l_spread)

    palette = {}
    palette.update(monotones)
    palette.update(accents)
    palette.update(br_accents)

    for name, (l,a,b) in palette.iteritems():
        palette[name] = [l, a*saturation, b*saturation]

    return palette

