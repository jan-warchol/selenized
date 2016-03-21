#!/usr/bin/python

# usage example:
#     echo "#D3D4D5 #1f3649" > color_mapping
#     ./colorchanger.py color_mapping example2

import os
import sys
import re
from pprint import pprint as pprint

color_re_dec = re.compile(r'(\d+),(\d+),(\d+)')
color_re_hex = re.compile(r'#?' + r'([0-9,a-f,A-F]{2})'*3)

def read_color(color):
    return [int(i,16) for i in color_re_hex.match(color).group(1, 2, 3)]

assert len(sys.argv) == 3
filepath = sys.argv[2]

with open(sys.argv[1]) as f:
    raw_mapping = [l.split() for l in f.read().rstrip().split('\n') if len(l)]

mapping = [(read_color(a), read_color(b)) for (a, b) in raw_mapping] 

def gen_all_formats(color, approx=0):
    # generacja roznych przestrzeni kolorow:
    r, g, b = color
    r1, g1, b1 = float(r)/255, float(g)/255, float(b)/255
    result = []
    # wszystkie mozliwe formaty:
    result.append("{0:02x}{1:02x}{2:02x}".format(r, g, b))  # lowercase hex
    result.append("{0:02x}{0:02x}{1:02x}{1:02x}{2:02x}{2:02x}".format(r, g, b))  # gnome-terminal
    result.append("{0:02X}{1:02X}{2:02X}".format(r, g, b))  # uppercase hex
    result.append("{0:d},{1:d},{2:d}".format(r, g, b))  # decimal (with commas)
    result.append("{0}, {1}, {2}".format(r1, g1, b1))  # [0, 1] floats (with commas)
    # iterm config format (each color separately)
    for component in (r1, g1, b1):
        pattern = str(component)
        # only try to match first <approx> decimal places
        if len(pattern) > approx+2 and approx != 0:
            pattern = pattern[:approx+2]
            pattern += "\d*"
        result.append('<real>{}'.format(pattern))
    return result

def replace_color(from_color, to_color, content):
    repl_dict = dict(zip(
        gen_all_formats(from_color, approx=6),
        gen_all_formats(to_color)
    ))

    def repl(matcher):
        return repl_dict[matcher.group(0)]

    print 'Replacing color', from_color, 'with', to_color, '.',
    print 'Full replacement dict:'
    pprint(repl_dict)

    for regex in repl_dict.keys():
        content = re.sub(re.compile(regex), repl_dict[regex], content)
    return content

ifile = open(filepath, 'r')
filecontent = ifile.read()
ifile.close()

for color_pair in mapping:
    from_color, to_color = color_pair
    filecontent = replace_color(from_color, to_color, filecontent)

ofile = open(filepath, 'w')
ofile.write(filecontent)
ofile.close()
