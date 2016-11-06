#!/usr/bin/python

import os
import sys
import re
import convert
import importlib

USAGE = """Evaluate templates using specified palette.

Takes two or more arguments:
$1 - name of the palette module to use
$2 [$3 ...] - path to a template file or to a folder that will be
recursively searched for templates."""

TMPL_EXT = '.template'

DEFAULT_OUTPUT_PREFIX = 'configs'

MARKER_RE = re.compile(r'!!COL(?P<delim>.)(?P<format>.*?)(?P=delim)')

def load_palette_from_module(module_name):
    m = importlib.import_module(module_name)
    palette = {
        name: convert.Color(color, name) for name, color in m.palette.iteritems()
    }

    # Add more attributes that can be used in templates
    for name, color in palette.iteritems():
        print "{:<12}{}".format(name, color)
        color.r  = int(round(color.srgb.rgb_r*255))
        color.g  = int(round(color.srgb.rgb_g*255))
        color.b  = int(round(color.srgb.rgb_b*255))
        color.r1 = color.srgb.rgb_r
        color.g1 = color.srgb.rgb_g
        color.b1 = color.srgb.rgb_b
        color.rs = str(color.srgb.rgb_r)
        color.gs = str(color.srgb.rgb_g)
        color.bs = str(color.srgb.rgb_b)
        color.apple.r = color.apple.rgb_r
        color.apple.g = color.apple.rgb_g
        color.apple.b = color.apple.rgb_b

    # Storing palette name in the same dictionary as the colors doesn't look
    # like the best data structure ever, but it will allow accessing the name
    # inside templates easily.
    try:
        palette['name'] = m.name
    except AttributeError:
        palette['name'] = module_name

    return palette

def load_palette_from_path(path):
    module_dir = os.path.dirname(path)
    if module_dir not in sys.path:
        sys.path.insert(0, module_dir)

    file_name = os.path.basename(path)
    module_name = re.sub(re.compile(r'\.py$'), '', file_name)
    return load_palette_from_module(module_name)

def process_template(palette, inpath, outpath=None):
    if not outpath:
        outpath = os.path.join(
            DEFAULT_OUTPUT_PREFIX,
            palette['name'] + '.' + os.path.basename(inpath)[:-(len(TMPL_EXT))]
        )

    def repl(matcher):
        return matcher.group('format').format(**palette)

    print "Processing {}...".format(inpath),
    with open(inpath, 'r') as ifile, open(outpath, 'w') as ofile :
        for line in ifile.readlines():
            try:
                ofile.write(re.sub(MARKER_RE, repl, line))
            except TypeError:
                print "ERROR: attribute not available in palette"
                sys.exit(1)
    print "result written to `{}.".format(outpath)

def process_directory(palette, directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if filepath.endswith(TMPL_EXT):
                process_template(palette, filepath)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print USAGE
        sys.exit()

    palette = load_palette_from_path(sys.argv[1])

    for path in sys.argv[2:]:
        if os.path.isfile(path):
            process_template(palette, path)
        else:
            process_directory(palette, path)

