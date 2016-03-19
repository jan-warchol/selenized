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
        self.appleR1 = float(r)/255  # TODO
        self.appleG1 = float(g)/255  # TODO
        self.appleB1 = float(b)/255  # TODO

scheme_source = {
    'bg': {
        0: (10, 10, 10),
        1: (100, 0, 0),
    },
    'lt_bg': {
        0: (200, 200, 200),
        1: (200, 100, 100),
    },
    'fg': {
        0: (211, 212, 213),
        1: (210, 110, 110),
    },
    'lt_fg': {
        0: (10, 10, 10),
        1: (100, 0, 0),
    },
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
