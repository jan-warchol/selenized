from __future__ import division

ACCENTS_MAX_REASONABLE_L = 75

def generate_palette(
    background,
    foreground="undefined",
    monotone_spec=None,
    saturation=1,
    accent_offset=0,
    accent_l_spread=None,
    br_accent_shift=None,
    br_bg_extra_saturation=1.2
):
    bg_l, bg_a, bg_b = background

    if foreground == "undefined":
        if bg_l <= 50:
            foreground = (bg_l+60, 0, 0)
        if bg_l > 50:
            foreground = (bg_l-60, 0, 0)

    fg_l, fg_a, fg_b = foreground


    # lightness relationships of many colors are expressed in terms of overall
    # palette contrast
    contrast = abs(fg_l - bg_l)

    # for palettes that have dark text on light background we invert lightness
    # changes (i.e. "bright" colors are darker)
    direction = -1 if bg_l > fg_l else 1



    ### MONOTONES

    monotones = {
        "bg": [bg_l, bg_a, bg_b],
        "fg": [fg_l, fg_a, fg_b],
    }

    if not monotone_spec:
        # define additional monotones using contrast
        # (0 - lightness like in bg, 1 - like in fg)
        # For some reason bright background looks washed out without increased saturation
        monotone_spec = {
            "bg_bright_1": [1/10,  br_bg_extra_saturation],
            "bg_bright_2": [1/4,   br_bg_extra_saturation],
            "fg_dim":      [5/8,   1],
            "fg_bright":   [1+1/5, 1],
        }

    # use weighted average.
    def expand_monotone(spec):
        relative_lightness, extra_saturation = spec
        l = bg_l + relative_lightness * (fg_l - bg_l)
        fg_weight = min(relative_lightness, 1)
        bg_weight = max(1 - relative_lightness, 0)
        a = (fg_weight*fg_a + bg_weight*bg_a) * extra_saturation
        b = (fg_weight*fg_b + bg_weight*bg_b) * extra_saturation
        return [l, a, b]

    for name in monotone_spec:
        monotones[name] = expand_monotone(monotone_spec[name])



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
        "violet":   [accent_base_l - 0.66*accent_l_spread,  30, -45],
        "magenta":  [accent_base_l - 0.50*accent_l_spread,  55, -15],
    }

    # bright accents have the same a* b* coords as regular accents and
    # uniformly shifted lightness
    if not br_accent_shift:
        br_accent_shift = contrast/10

    br_accents = {
        'br_'+name: [l + direction*br_accent_shift, a, b]
        for name, [l, a, b]
        in accents.items()
    }

    # optionally scale all colors
    scaling = 1

    for key, value in monotones.items():
        monotones[key][0] = fg_l - (fg_l - value[0])*scaling

    for key, value in accents.items():
        accents[key][0] = fg_l - (fg_l - value[0])*scaling


    ### FINAL ASSEMBLY

    # some debug
    acc_bg_dists = [float(abs(accents[color][0]-bg_l)) for color in accents]
    acc_hi_dists = [float(abs(accents[color][0]-monotones["bg_bright_2"][0])) for color in accents]

    print("""Foreground: {}
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
        monotones["bg"][0],
        contrast,
        float(accent_base_l),
        float(accent_base_l - accent_l_spread),

        float(abs(fg_l-monotones["fg_dim"][0])),
        float(abs(monotones["bg_bright_2"][0]-bg_l)),
        float(abs(monotones["bg_bright_2"][0]-monotones["fg_dim"][0])),
        min(acc_hi_dists),
        max(acc_hi_dists),
        min(acc_bg_dists),
        max(acc_bg_dists),
    ))

    palette = {}
    palette.update(monotones)
    palette.update(accents)
    palette.update(br_accents)

    for name, (l,a,b) in palette.items():
        palette[name] = [l, a*saturation, b*saturation]

    return palette

