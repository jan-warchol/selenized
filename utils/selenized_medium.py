#!/usr/bin/python

# LAB lightness of background (0-100)
bg_l = 25
# difference in LAB lightness between foreground and background
contrast = 50
# difference in LAB lightness between regular and bright accent colors
br_contrast = 5

fg_l = bg_l + contrast

monotones = {
    "bg":       [bg_l,    -10, -16],
    "black":    [bg_l+10, -12, -19],
    "br_black": [fg_l-15,  -7,  -9],
    "fg":       [fg_l,     -6,  -6],
    "white":    [fg_l,     -6,  -6],
    "br_white": [fg_l+10,  -6,  -6],
}

accents = {
    "red":      [fg_l-14,  63,  40],
    "orange":   [fg_l-8,   37,  50],
    "yellow":   [fg_l-1,    6,  65],
    "green":    [fg_l-6,  -37,  53],
    "cyan":     [fg_l-2,  -40,  -4],
    "blue":     [fg_l-14,   0, -55],
    "violet":   [fg_l-11,  33, -48],
    "magenta":  [fg_l-10,  59, -21],
}

# bright accents have the same a* b* coords as regular accents
br_accents = {
    'br_'+name: [l+br_contrast, a, b]
    for name, [l, a, b]
    in accents.iteritems()
}

palette = {}
palette.update(monotones)
palette.update(accents)
palette.update(br_accents)

