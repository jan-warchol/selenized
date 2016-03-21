#!/usr/bin/python

import os
import sys
import re

tmpl_ext = '.template'

marker_re = re.compile(r'!!COL(?P<delim>.)(?P<format>.*?)(?P=delim)')

class Color:
    def __init__(self, rgb):
        r, g, b = rgb
        self.r = r
        self.g = g
        self.b = b
        self.r1 = float(r)/255
        self.g1 = float(g)/255
        self.b1 = float(b)/255
        self.rs = str(self.r1)
        self.gs = str(self.g1)
        self.bs = str(self.b1)

scheme_source = {
    'bg':         { 0: ( 31, 54, 73) },
    'black':      { 0: ( 50, 75, 96) },
    'br_black':   { 0: (109,140,166) },
    'fg':         { 0: (164,183,199) },
    'white':      { 0: (164,183,199) },
    'br_white':   { 0: (196,216,234) },

    'red':        { 0: (255, 62, 61) },
    'green':      { 0: (110,185, 43) },
    'yellow':     { 0: (215,170, 37) },
    'blue':       { 0: ( 77,137,255) },
    'magenta':    { 0: (222, 93,253) },
    'cyan':       { 0: ( 75,200,180) },

    'br_red':     { 0: (255, 76, 72) },
    'br_green':   { 0: (124,202, 56) },
    'br_yellow':  { 0: (234,186, 49) },
    'br_blue':    { 0: ( 92,152,255) },
    'br_magenta': { 0: (240,108,255) },
    'br_cyan':    { 0: ( 89,217,196) },
}

def compile_scheme(scheme):
    if isinstance(scheme, dict):
        return {k: compile_scheme(v) for k, v in scheme.iteritems()}
    else:
        return Color(scheme)

scheme = compile_scheme(scheme_source)

def repl(matcher):
    return matcher.group('format').format(**scheme)

for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        if filepath.endswith(tmpl_ext):
            resultpath = filepath[:-(len(tmpl_ext))]
            ifile = open(filepath, 'r')
            ofile = open(resultpath, 'w')
            for line in ifile.readlines():
                ofile.write(re.sub(marker_re, repl, line))
            ifile.close()
            ofile.close()
