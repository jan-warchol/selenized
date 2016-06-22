#!/usr/bin/python

from __future__ import division
from colormath.color_objects import LabColor, sRGBColor, AppleRGBColor, BaseRGBColor, HSVColor
from colormath.color_conversions import convert_color
import re
import sys

USAGE = """Convert color(s) to all color spaces used by Selenized.

The argument can be:
  - a string representation of a color (e.g. c4d8df for sRGB, 23,-8,15 for Lab)
  - a path to a file with one color per line (empty lines allowed)"""


# Define some pretty printing for classes from colormath module.
def lab_str(self):
    return "{:>3.0f} {:>3.0f} {:>3.0f}".format(
        self.lab_l, self.lab_a, self.lab_b
    )

def hsv_str(self):
    return "{:>3.0f} {:>3.0f} {:>3.0f}".format(
        self.hsv_h, self.hsv_s*100, self.hsv_v*100
    )

# def rgb_str(self):
#     return "{:>3.0f},{:>3.0f},{:>3.0f}".format(
#         self.rgb_r*255, self.rgb_g*255, self.rgb_b*255
#     )

LabColor.__str__      = lab_str
HSVColor.__str__      = hsv_str
sRGBColor.__str__     = sRGBColor.get_rgb_hex
AppleRGBColor.__str__ = AppleRGBColor.get_rgb_hex


def parse_string(s):
    """Extract 3 integers (hex or decimal) from a string.

    Interprets strings beginning with a hash as hexadecimal,
    strings separated with whitespace and/or commas as decimal."""

    hex_num = r'([0-9a-fA-F]{2})'
    dec_num = r'(-?[0-9]{1,3})'
    hex_color_re = re.compile(r'#?' + hex_num*3)
    dec_color_re = re.compile(',?\s*'.join([dec_num]*3))

    coords = hex_color_re.match(s)
    if coords:
        base = 16
    else:
        coords = dec_color_re.match(s)
        base = 10

    parsed = [int(i, base) for i in coords.group(1, 2, 3)]

    return parsed, base


class Color(object):
    # some of the bright versions of colors are slightly out of RGB gamut -
    # it's not a big deal, we just clamp them.
    @staticmethod
    def clamp(color):
        color.rgb_r = color.clamped_rgb_r
        color.rgb_g = color.clamped_rgb_g
        color.rgb_b = color.clamped_rgb_b
        return color

    def __init__(self, spec):
        # decide how to interpret it (rgb or lab?)
        if isinstance(spec, list):
            spec = LabColor(*spec, illuminant='d50')
        elif isinstance(spec, str):
            parsed, base = parse_string(spec)
            if base == 16:
                spec = sRGBColor(*[i/255 for i in parsed])
            else:
                spec = LabColor(*parsed, illuminant='d50')

        # convert to all needed spaces
        self.lab = convert_color(spec, LabColor, target_illuminant='d50')
        self.srgb = Color.clamp(convert_color(spec, sRGBColor))
        self.apple = Color.clamp(convert_color(spec, AppleRGBColor))
        self.hsv = convert_color(spec, HSVColor)

    def __str__(self):
        return "   ".join(["{}"]*4).format(
            self.lab,
            self.hsv,
            self.srgb,
            self.apple,
        )

    def __repr__(self):
        return "\n".join(["{}"]*4).format(
            repr(self.lab),
            repr(self.hsv),
            repr(self.srgb),
            repr(self.apple),
        )


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print USAGE
        sys.exit()

    if len(sys.argv) == 2:
        arg = sys.argv[1]
        try:
            with open(arg) as f:
                colors = [Color(l) for l in f.read().rstrip().split('\n') if len(l)]
        except IOError:
            colors = [Color(arg)]

        for c in colors:
            print(c)

    else:
        import selenized_medium
        palette = {
            name: Color(color)
            for name, color
            in selenized_medium.palette.iteritems()
        }

        for name, color in palette.iteritems():
            print "{:<12}{}".format(name, color)

