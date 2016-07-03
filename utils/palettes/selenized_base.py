def generate_palette(background, foreground, br_accent_incr=5):
    bg_l, bg_a, bg_b = background
    fg_l, fg_a, fg_b = foreground

    background_tones = {
        "bg":       [bg_l,    bg_a,     bg_b    ],
        "black":    [bg_l+10, bg_a*1.2, bg_b*1.2],
    }

    content_tones = {
        "br_black": [fg_l-15, fg_a*1.2, fg_b*1.5],
        "fg":       [fg_l,    fg_a,     fg_b    ],
        "white":    [fg_l,    fg_a,     fg_b    ],
        "br_white": [fg_l+10, fg_a,     fg_b    ],
    }

    accent_base_l = fg_l
    accents = {
        "red":      [accent_base_l - 14,  63,  40],
        "orange":   [accent_base_l -  8,  37,  50],
        "yellow":   [accent_base_l -  1,   6,  65],
        "green":    [accent_base_l -  6, -37,  53],
        "cyan":     [accent_base_l -  2, -40,  -4],
        "blue":     [accent_base_l - 14,   0, -55],
        "violet":   [accent_base_l - 11,  33, -48],
        "magenta":  [accent_base_l - 10,  59, -21],
    }

    # bright accents have the same a* b* coords as regular accents
    br_accents = {
        'br_'+name: [l+br_accent_incr, a, b]
        for name, [l, a, b]
        in accents.iteritems()
    }

    palette = {}
    palette.update(background_tones)
    palette.update(content_tones)
    palette.update(accents)
    palette.update(br_accents)

    return palette

