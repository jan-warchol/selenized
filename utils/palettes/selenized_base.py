from __future__ import division

def generate_palette(background, foreground, saturation=1, accent_offset=0, br_accent_shift=None):
    bg_l, bg_a, bg_b = background
    fg_l, fg_a, fg_b = foreground

    # lightness relationships of many colors are expressed in terms of overall
    # palette contrast
    contrast = abs(fg_l - bg_l)

    # for palettes that have dark text on light background we invert lightness
    # changes (i.e. "bright" colors are darker)
    direction = -1 if bg_l > fg_l else 1

    background_tones = {
        "bg":       [bg_l,                        bg_a,     bg_b    ],
        "black":    [bg_l + direction*contrast/5, bg_a*1.2, bg_b*1.2],
    }

    content_tones = {
        "br_black": [fg_l - direction*contrast/3, fg_a*1.2, fg_b*1.5],
        "fg":       [fg_l,                        fg_a,     fg_b    ],
        "white":    [fg_l,                        fg_a,     fg_b    ],
        "br_white": [fg_l + direction*contrast/5, fg_a,     fg_b    ],
    }

    # accent colors shouldn't have exactly uniform lightness, but on the other
    # hand they shouldn't be too far away from each other.
    accent_l_spread = contrast/3

    # in dark palettes, brightest accents should have lightness close to
    # foreground. In light palettes it should be the darkest accents.
    accent_base_l = fg_l if direction == 1 else fg_l + accent_l_spread

    # optionally move accent colors lightness away from foreground lightness
    accent_base_l -= direction*accent_offset

    accents = {
        "red":      [accent_base_l - 0.84*accent_l_spread,  63*saturation,  40*saturation],
        "orange":   [accent_base_l - 0.48*accent_l_spread,  37*saturation,  50*saturation],
        "yellow":   [accent_base_l - 0.06*accent_l_spread,   6*saturation,  65*saturation],
        "green":    [accent_base_l - 0.36*accent_l_spread, -37*saturation,  53*saturation],
        "cyan":     [accent_base_l - 0.12*accent_l_spread, -40*saturation,  -4*saturation],
        "blue":     [accent_base_l - 0.84*accent_l_spread,   0*saturation, -55*saturation],
        "violet":   [accent_base_l - 0.66*accent_l_spread,  33*saturation, -48*saturation],
        "magenta":  [accent_base_l - 0.60*accent_l_spread,  59*saturation, -21*saturation],
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

    # some debug
    print "Foreground:", fg_l
    print "Background:", bg_l
    print "Contrast:", contrast
    print "Accents max lightness:", accent_base_l
    print "Accents min lightness: {:.3}".format(accent_base_l - accent_l_spread)
    print ""

    palette = {}
    palette.update(background_tones)
    palette.update(content_tones)
    palette.update(accents)
    palette.update(br_accents)

    return palette

