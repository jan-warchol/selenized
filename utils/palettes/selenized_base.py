from __future__ import division

ACCENTS_MAX_REASONABLE_L = 75

def generate_palette(
    background,
    foreground,
    saturation=1,
    accent_offset=0,
    accent_l_spread=None,
    br_accent_shift=None,
    br_bg_extra_saturation=1.1
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
    br_bg_l = bg_l + direction*contrast/10
    br_bg_a, br_bg_b = bg_a*br_bg_extra_saturation, bg_b*br_bg_extra_saturation

    hi_bg_l = bg_l + direction*contrast/4

    br_fg_l = fg_l + direction*contrast/5

    # color used for comments and other secondary content; it's a weighted
    # average of fg and bg
    dim_fg_l = 3/8 * bg_l + 5/8 * fg_l
    dim_fg_a = 3/8 * bg_a + 5/8 * fg_a
    dim_fg_b = 3/8 * bg_b + 5/8 * fg_b

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
    if not accent_l_spread:
        accent_l_spread = abs(accent_base_l - bg_l)/3

    # in dark-on-light palettes it's the darkest accents that should have
    # lightness close to foreground
    if direction == -1:
        accent_base_l += accent_l_spread

    accents = {
        "red":      [accent_base_l - 0.84*accent_l_spread,  63,  40],
        "orange":   [accent_base_l - 0.48*accent_l_spread,  37,  50],
        "yellow":   [accent_base_l - 0.00*accent_l_spread,   6,  68],
        "green":    [accent_base_l - 0.36*accent_l_spread, -38,  55],
        "cyan":     [accent_base_l - 0.12*accent_l_spread, -40,  -4],
        "blue":     [accent_base_l - 0.84*accent_l_spread,   0, -57],
        "violet":   [accent_base_l - 0.66*accent_l_spread,  33, -48],
        "magenta":  [accent_base_l - 0.50*accent_l_spread,  55, -15],
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
    acc_bg_dists = [float(abs(accents[color][0]-bg_l)) for color in accents]
    acc_hi_dists = [float(abs(accents[color][0]-hi_bg_l)) for color in accents]

    print """Foreground: {}
Background: {}
Contrast: {}
Accents max lightness: {:.3}
Accents min lightness: {:.3}

Foreground-comment distance:     {:.3}
Highlight contrast:              {:.3}
Highlight-comment distance:      {:.3}
Highlight-accent distance:   min {:.3}, max {:.3}
Background-accent distance:  min {:.3}, max {:.3}
    """.format(
        fg_l,
        bg_l,
        contrast,
        float(accent_base_l),
        float(accent_base_l - accent_l_spread),

        float(abs(fg_l-dim_fg_l)),
        float(abs(hi_bg_l-bg_l)),
        float(abs(hi_bg_l-dim_fg_l)),
        min(acc_hi_dists),
        max(acc_hi_dists),
        min(acc_bg_dists),
        max(acc_bg_dists),
    )

    palette = {}
    palette.update(monotones)
    palette.update(accents)
    palette.update(br_accents)

    for name, (l,a,b) in palette.iteritems():
        palette[name] = [l, a*saturation, b*saturation]

    return palette

