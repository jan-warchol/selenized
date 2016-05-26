from colormath.color_objects import LabColor, sRGBColor, AppleRGBColor, BaseRGBColor, HSVColor
from colormath.color_conversions import convert_color
from copy import copy as copy

# yeah, I know it's not the best code in the world, but it gets the job done.
# TODO: change to be more OOP

# LAB lightness of background (0-100)
bg_l = 25
# difference in LAB lightness between foreground and background
contrast = 50
# difference in LAB lightness between regular and bright accent colors
bright_contrast = 5

fg_l = bg_l + contrast

monotones = [
    ["bg",       LabColor(bg_l,    -10, -16, illuminant='d50')],
    ["black",    LabColor(bg_l+10, -12, -19, illuminant='d50')],
    ["br_black", LabColor(fg_l-15,  -7,  -9, illuminant='d50')],
    ["fg",       LabColor(fg_l,     -6,  -6, illuminant='d50')],
    ["white",    LabColor(fg_l,     -6,  -6, illuminant='d50')],
    ["br_white", LabColor(fg_l+10,  -6,  -6, illuminant='d50')],
]

accent_colors = [
    ["red",      LabColor(fg_l-14,  63,  40, illuminant='d50')],
    ["green",    LabColor(fg_l-6,  -37,  53, illuminant='d50')],
    ["yellow",   LabColor(fg_l-1,    6,  65, illuminant='d50')],
    ["blue",     LabColor(fg_l-14,   0, -55, illuminant='d50')],
    ["magenta",  LabColor(fg_l-10,  59, -21, illuminant='d50')],
    ["cyan",     LabColor(fg_l-2,  -40,  -4, illuminant='d50')],
    ["orange",   LabColor(fg_l-8,   37,  50, illuminant='d50')],
    ["violet",   LabColor(fg_l-11,  33, -48, illuminant='d50')],
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

def print_hsv_color(self):
    return "{:>3.0f} {:>3.0f} {:>3.0f}".format(
        self.hsv_h,
        min(self.hsv_s * 100, 100),
        min(self.hsv_v * 100, 100)
    )

def print_rgb_color(self):
    return "{:>3.0f},{:>3.0f},{:>3.0f}".format(
        self.rgb_r * 255,
        self.rgb_g * 255,
        self.rgb_b * 255
    )

def print_rgb_color_float(self):
    return "{:<14} {:<14} {:<14}".format(
        self.rgb_r,
        self.rgb_g,
        self.rgb_b
    )

LabColor.str = print_lab_color
HSVColor.str = print_hsv_color
BaseRGBColor.str = print_rgb_color
BaseRGBColor.floats = print_rgb_color_float

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
    result.append(srgb)
    srgb_hex = sRGBColor.get_rgb_hex(srgb)
    result.append(srgb_hex)

    applergb = clamp_rgb_color(convert_color(lab, AppleRGBColor))
    result.append(applergb)
    applergb_hex = AppleRGBColor.get_rgb_hex(applergb)
    result.append(applergb_hex)

    hsb = convert_color(lab, HSVColor)
    result.append(hsb)
    # print color, hsb.str()
    # applergb_hex = HSVColor.get_rgb_hex(applergb)
    # result.append(applergb_hex)

    return result

full_palete = [add_rgb(color) for color in palette]

print "Color        CIE L*a*b*   sRGB      AppleRGB  HSB"
print "----------   ----------   -------   --------  -----------"
for name, lab, srgb, srgb_hex, apple, apple_hex, hsb in full_palete:
    print '{:<10}   {}   {}   {}   {}'.format(name, lab.str(), srgb_hex, apple_hex, hsb.str())

print ""
print "Color        sRGB"
print "----------   --------------------------------"
for name, lab, srgb, srgb_hex, apple, apple_hex, hsb in full_palete:
    print '{:<10}   {}   {}   {}'.format(
        name,
        srgb_hex,
        srgb.str(),
        srgb.floats()
    )

print ""
print "Color        Apple RGB"
print "----------   --------------------------------"
for name, lab, srgb, srgb_hex, apple, apple_hex, hsb in full_palete:
    print '{:<10}   {}   {}   {}'.format(
        name,
        apple_hex,
        apple.str(),
        apple.floats()
    )
