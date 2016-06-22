#!/usr/bin/python

import os
import sys
import re
import convert
import selenized_medium

USAGE = """Evaluate templates using selenized palette.

Takes one argument - path to a template file or to a folder that will be
recursively searched for templates."""

TMPL_EXT = '.template'

MARKER_RE = re.compile(r'!!COL(?P<delim>.)(?P<format>.*?)(?P=delim)')

palette = {
    name: {0: convert.Color(color)}
    for name, color
    in selenized_medium.palette.iteritems()
}

for name, color in palette.iteritems():
    # print "{:<12}{}".format(name, color)
    color[0].r  = int(round(color[0].srgb.rgb_r*255))
    color[0].g  = int(round(color[0].srgb.rgb_g*255))
    color[0].b  = int(round(color[0].srgb.rgb_b*255))
    color[0].r1 = color[0].srgb.rgb_r
    color[0].g1 = color[0].srgb.rgb_g
    color[0].b1 = color[0].srgb.rgb_b
    color[0].rs = str(color[0].srgb.rgb_r)
    color[0].gs = str(color[0].srgb.rgb_g)
    color[0].bs = str(color[0].srgb.rgb_b)

def repl(matcher):
    return matcher.group('format').format(**palette)

def process_template(filepath):
    print "Processing {}...".format(filepath)
    resultpath = filepath[:-(len(TMPL_EXT))]
    with open(filepath, 'r') as ifile, open(resultpath, 'w') as ofile :
        for line in ifile.readlines():
            try:
                ofile.write(re.sub(MARKER_RE, repl, line))
            except TypeError:
                print "ERROR: attribute not available in palette"
                sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print USAGE
        sys.exit()
    elif os.path.isfile(sys.argv[1]):
        process_template(sys.argv[1])
    else:
        for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if filepath.endswith(TMPL_EXT):
                    process_template(filepath)

