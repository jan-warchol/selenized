from colormath.color_objects import LabColor, sRGBColor, AppleRGBColor, BaseRGBColor, HSVColor
from colormath.color_conversions import convert_color
import selenized_medium
from pprint import pprint as pp

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
def add_rgb(name, lab_coords):
    lab = LabColor(*lab_coords, illuminant='d50')
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

full_palete = [add_rgb(name, coords) for name, coords in selenized_medium.palette.iteritems()]

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
