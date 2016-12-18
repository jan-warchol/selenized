import selenized_base

name = 'Selenized light'

palette = selenized_base.generate_palette(
    background=(96,  0, 12),
    foreground=(42, -6, -6),
    accent_offset=3,
    br_accent_shift=2,
    accent_l_spread=10,
    br_bg_extra_saturation=1,
)

