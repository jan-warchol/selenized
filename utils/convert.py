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
    # Note that we don't need to check for negative values because colormath
    # does this for us.
    def clamp(self, space):
        WARN_THRESHOLD = 1.02
        color = getattr(self, space)
        coord_names = []
        if isinstance(color, BaseRGBColor):
            coord_names = ['rgb_r', 'rgb_g', 'rgb_b']

        for name in coord_names:
            coord = getattr(color, name)
            if coord > WARN_THRESHOLD:
                print ("Warning: {:.2}% out of gamut" .format((coord-1)*100))
            setattr(color, name, min(coord, 1))
        return color

    def __init__(self, spec, name=None):
        self.name = name if name else spec
        # decide how to interpret it (rgb or lab?)
        if isinstance(spec, list):
            spec = LabColor(*spec, illuminant='d50')
        elif isinstance(spec, str):
            parsed, base = parse_string(spec)
            if base == 16:
                spec = sRGBColor(*[i/255 for i in parsed])
            else:
                spec = LabColor(*parsed, illuminant='d50')

        print "Converting {}...".format(self.name)
        # convert to all needed spaces
        self.lab = convert_color(spec, LabColor, target_illuminant='d50')
        self.srgb = convert_color(spec, sRGBColor)
        self.apple = convert_color(self.lab, AppleRGBColor)
        self.hsv = convert_color(spec, HSVColor)

        # some of the bright versions of colors are slightly out of RGB gamut -
        # it's not a big deal, we just clamp them.
        self.clamp('srgb')
        self.clamp('apple')
        self.clamp('hsv')

    def __str__(self):
        return "   ".join(["{}"]*4).format(
            self.lab,
            self.hsv,
            self.srgb,
            self.apple,
        )

    def __repr__(self):
        return ("<Selenized Color Coords:" + "\n    {}"*4 + "\n>").format(
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

        header = (
            "CIE L*a*b*    HSV           sRGB      AppleRGB\n"
            "-----------   -----------   -------   --------"
        )
        print '\n', header
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

