from __future__ import division

def calc_lightness(transparency):
    # background
    nominal_bg_l = 0
    bg_min_l = nominal_bg_l*transparency
    bg_max_l = 100*transparency + nominal_bg_l
    avg_bg_l = (bg_min_l + bg_max_l) / 2

    # foreground
    fg_min_contrast = 50
    fg_desired_contrast = 66
    fg_desired_l = avg_bg_l + fg_desired_contrast
    fg_l = max(fg_desired_l, bg_max_l + fg_min_contrast)

    # comment
    min_comment_contrast = 30
    comment_desired_contrast = (fg_l - avg_bg_l) * 2/3
    comment_desired_l = avg_bg_l + comment_desired_contrast
    comment_l = max(comment_desired_l, bg_max_l + min_comment_contrast)

    # selection

    # background highlight

    # contrast of text in background
    double_nelson = (fg_l - avg_bg_l) * transparency

    # results
    print(f"""transparency: {transparency}
bg_max_l: {bg_max_l}
comment_l: {comment_l}
fg_l: {fg_l}
window_below: {double_nelson}
    """)


calc_lightness(0.2)
calc_lightness(0.25)
calc_lightness(0.30)
calc_lightness(0.33)
calc_lightness(0.4)
