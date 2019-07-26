Utility scripts for selenized
-----------------------------

Scripts for converting between color spaces and generating config files from
templates.



### Requirements

- [Python](https://www.python.org/) with development files. Python 3.7
  and 2.7 is known works; 3.5 and 3.6 might work, but nobody tried yet,
- [Colormath](https://github.com/gtaylor/python-colormath) Python library.

Example requirements installation for Debian/Ubuntu Linux and Python 2.7:

    # ensure your environment has all necessary tools
    sudo apt-get install git python2.7 python-dev python-pip

    # install colormath with AppleRGB color space support
    sudo pip install --upgrade colormath



### Generating config files

To generate config file, use `evaluate_template.py` script. You need to provide
it with two arguments: path to the palette module (with the palette you want to
use) and path to a template config for your terminal. For example, if you
wanted to generate selenized medium config file for iTerm, you would do it like
this:

    selenized/utils$ python evaluate_template.py \
                         palettes/selenized_medium.py \
                         templates/itermcolors.template
    [...]
    Processing templates/itermcolors.template...
    Result written to output/Selenized medium.itermcolors

Then you need to install the config (see instructions in [top-level
README](../README.md#installation)).



### Converting a color between spaces

From Lab:

    selenized/utils$ python convert_color.py "25,-10,-16"

    CIE L*a*b*    HSV           sRGB      AppleRGB
    -----------   -----------   -------   --------
     25 -10 -16   198  74  33   #154053   #143242

From sRGB (must be given in hex format):

    selenized/utils$ python convert_color.py "a8bcc3"

    CIE L*a*b*    HSV           sRGB      AppleRGB
    -----------   -----------   -------   --------
     75  -6  -6   196  14  76   #a8bcc3   #99aeb6
