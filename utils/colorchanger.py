#!/usr/bin/python

# usage example: ./colorchanger.py 211,212,213 111,112,113 example2

import os
import sys
import re


color_re = re.compile(r'(\d+),(\d+),(\d+)')

def read_color(color):
    return [int(i) for i in color_re.match(color).group(1, 2, 3)]

assert len(sys.argv) == 4
color_change_from = read_color(sys.argv[1])
color_change_to = read_color(sys.argv[2])
filepath = sys.argv[3]

def gen_all_formats(color):
    # generacja roznych przestrzeni kolorow:
    r, g, b = color
    r1, g1, b1 = float(r)/255, float(g)/255, float(b)/255
    result = []
    # wszystkie mozliwe formaty:
    result.append("{0:02x}{1:02x}{2:02x}".format(r, g, b))  # lowercase hex
    result.append("{0:02x}{0:02x}{1:02x}{1:02x}{2:02x}{2:02x}".format(r, g, b))  # gnome-terminal
    result.append("{0:02X}{1:02X}{2:02X}".format(r, g, b))  # uppercase hex
    result.append("{0:d}, {1:d}, {2:d}".format(r, g, b))  # decimal (with commas)
    result.append("{0:f}, {1:f}, {2:f}".format(r1, g1, b1))  # [0, 1] floats (with commas)
    return result

repl_dict = dict(zip(gen_all_formats(color_change_from), gen_all_formats(color_change_to)))

def repl(matcher):
    return repl_dict[matcher.group(0)]

print repl_dict

regex = re.compile('|'.join(repl_dict.keys()))

ifile = open(filepath, 'r')
filecontent = ifile.read()
ifile.close()
filecontent = re.sub(regex, repl, filecontent)
ofile = open(filepath, 'w')
ofile.write(filecontent)
ofile.close()
