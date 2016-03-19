from colormath.color_objects import LabColor, sRGBColor, AppleRGBColor
from colormath.color_conversions import convert_color
from copy import copy as copy

# LAB lightness of background (0-100)
bg_l = 28
# difference in LAB lightness between foreground and background
contrast = 50
# difference in LAB lightness between regular and bright accent colors
bright_contrast = 5

fg_l = bg_l + contrast

monotones = [
    ["bg",       LabColor(bg_l,    -7, -16, illuminant='d50')],
    ["black",    LabColor(bg_l+10, -7, -16, illuminant='d50')],
    ["br_black", LabColor(fg_l-15, -7, -16, illuminant='d50')],
    ["fg",       LabColor(fg_l,    -4, -9,  illuminant='d50')],
    ["white",    LabColor(fg_l,    -4, -9,  illuminant='d50')],
    ["br_white", LabColor(fg_l+10, -4, -9,  illuminant='d50')]
]

accent_colors = [
    ["red",     LabColor(fg_l-15,  66,  44, illuminant='d50')],
    ["green",   LabColor(fg_l-6,  -40,  54, illuminant='d50')],
    ["yellow",  LabColor(fg_l-1,    6,  65, illuminant='d50')],
    ["blue",    LabColor(fg_l-14,   4, -59, illuminant='d50')],
    ["magenta", LabColor(fg_l-10,  58, -46, illuminant='d50')],
    ["cyan",    LabColor(fg_l-2,  -40,  -4, illuminant='d50')]
]

# bright colors are derived from regular (+5 Lab lightness)
bright_accents = [('br_'+name, copy(color)) for name, color in accent_colors]
for name, color in bright_accents:
    color.lab_l += bright_contrast

palette = []
palette.extend(monotones)
palette.extend(accent_colors)
palette.extend(bright_accents)

# just some pretty printing
def print_lab_color(self):
    return "{:.0f} {:>3.0f} {:>3.0f}".format(
        self.lab_l,
        self.lab_a,
        self.lab_b
    )

LabColor.str = print_lab_color

# some of the bright versions of colors are slightly out of RGB gamut -
# it's not a big deal, we just clamp them.
def clamp_rgb_color(color):
    color.rgb_r = color.clamped_rgb_r
    color.rgb_g = color.clamped_rgb_g
    color.rgb_b = color.clamped_rgb_b
    return color

# calculate sRGB and AppleRGB coordinates
def add_rgb(color):
    name, lab = color
    result = [name, lab]

    srgb = clamp_rgb_color(convert_color(lab, sRGBColor))
    srgb_hex = sRGBColor.get_rgb_hex(srgb)
    result.append(srgb_hex)

    applergb = clamp_rgb_color(convert_color(lab, AppleRGBColor))
    applergb_hex = AppleRGBColor.get_rgb_hex(applergb)
    result.append(applergb_hex)

    return result

full_palete = [add_rgb(color) for color in palette]

print "Color        CIE L*a*b*   sRGB      Apple RGB"
print "----------   ----------   -------   ---------"
for name, lab, srgb, apple in full_palete:
    print '{:<10}   {}   {}   {}'.format(name, lab.str(), srgb, apple)

