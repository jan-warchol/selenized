from __future__ import division
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color
import re
import sys

USAGE = """Convert from sRGB to Lab or from Lab to sRGB.

The argument should either be a color (e.g. #c4d8df for sRGB, 23,-8,15 for Lab)
or a path to a file with one color per line (empty lines allowed)."""

if len(sys.argv) != 2:
    print USAGE
    sys.exit()

hex_num = r'([0-9a-fA-F]{2})'
dec_num = r'(-?[0-9]{1,3})'
hex_color_re = re.compile(r'#?' + hex_num*3)
dec_color_re = re.compile(',\s*'.join([dec_num]*3))

def parse_color(color):
    coords = hex_color_re.match(color)
    if coords:
        base = 16
    else:
        coords = dec_color_re.match(color)
        base = 10

    parsed = [int(i, base) for i in coords.group(1, 2, 3)]
    if base == 16:
        return sRGBColor(*[i/255 for i in parsed])
    else:
        return LabColor(*parsed, illuminant='d50')

def convert(color):
    if isinstance(color, sRGBColor):
        return convert_color(color, LabColor, target_illuminant='d50')
    else:
        return convert_color(color, sRGBColor)

arg = sys.argv[1]
try:
    with open(arg) as f:
        colors = [parse_color(l) for l in f.read().rstrip().split('\n') if len(l)]
except IOError:
    colors = [parse_color(arg)]

print [convert(c) for c in colors]

