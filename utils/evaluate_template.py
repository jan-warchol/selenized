#!/usr/bin/env python

import os
import sys
import re
import convert_color
import importlib

USAGE = """Evaluate templates using specified palette.

Takes two or more arguments:
$1 - name of the palette module to use
$2 [$3 ...] - path to a template file or to a folder that will be
recursively searched for templates."""

TMPL_EXT = '.template'

DEFAULT_OUTPUT_DIR = ''

MARKER_RE = re.compile(r'!!COL(?P<delim>.)(?P<format>.*?)(?P=delim)')

DEFAULT_COLOR_ORDER = [
    'bg', 'bg_bright_1', 'bg_bright_2', 'fg_dim', 'fg', 'fg_bright',
    'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'orange', 'violet',
    'br_red', 'br_green', 'br_yellow', 'br_blue', 'br_magenta', 'br_cyan', 'br_orange', 'br_violet'
]

def load_palette_from_module(module_name):
    base_module_dir = os.path.join(os.path.dirname(sys.argv[0]), 'palettes')
    sys.path.insert(0, base_module_dir)
    m = importlib.import_module(module_name)
    palette = {
        name: convert_color.Color(color, name) for name, color in m.palette.items()
    }

    # Add more attributes that can be used in templates
    for name, color in palette.items():
        color.r  = int(round(color.srgb.rgb_r*255))
        color.g  = int(round(color.srgb.rgb_g*255))
        color.b  = int(round(color.srgb.rgb_b*255))
        color.r1 = color.srgb.rgb_r
        color.g1 = color.srgb.rgb_g
        color.b1 = color.srgb.rgb_b
        color.rs = str(color.srgb.rgb_r)
        color.gs = str(color.srgb.rgb_g)
        color.bs = str(color.srgb.rgb_b)
        color.apple.r = float(color.apple.rgb_r)
        color.apple.g = float(color.apple.rgb_g)
        color.apple.b = float(color.apple.rgb_b)

    # Storing palette name in the same dictionary as the colors doesn't look
    # like the best data structure ever, but it will allow accessing the name
    # inside templates easily.
    try:
        palette['name'] = m.name
    except AttributeError:
        palette['name'] = module_name

    print('Palette: ' + palette['name'] + '\n')
    for color in DEFAULT_COLOR_ORDER:
        if color in ['red', 'br_red']:
            print ('') # section separator
        if color in palette:
            print("{:<12}{}".format(color, palette[color]))

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
        name = palette['name'].lower().replace(' ', '-')
        templ_name = os.path.basename(inpath)[:-(len(TMPL_EXT))]
        out_extension = re.sub(re.compile(r'[^\.]*\.'), '', templ_name)
        outpath = os.path.join(
            DEFAULT_OUTPUT_DIR,
            name + '.' + out_extension
        )

    def repl(matcher):
        return matcher.group('format').format(**palette)

    print("\nProcessing {}...".format(inpath))
    with open(inpath, 'r') as ifile, open(outpath, 'w') as ofile :
        for line in ifile.readlines():
            try:
                ofile.write(re.sub(MARKER_RE, repl, line))
            except TypeError:
                print("ERROR: attribute not available in palette")
                sys.exit(1)
    print("Result written to {}".format(outpath))


def process_directory_recursively(palette, directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if filepath.endswith(TMPL_EXT):
                process_template(palette, filepath)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(USAGE)
        sys.exit()

    palette = load_palette_from_path(sys.argv[1])

    for path in sys.argv[2:]:
        if os.path.isfile(path):
            process_template(palette, path)
        else:
            process_directory_recursively(palette, path)

