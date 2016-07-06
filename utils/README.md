Utility scripts for selenized
-----------------------------

Scripts for converting between color spaces and generating config files from
templates.



### Setup

    # ensure your environment has all necessary tools
    sudo apt-get install git python2.7 python-dev python-pip

    # install colormath with AppleRGB color space support
    sudo pip install git+git://github.com/gtaylor/python-colormath@fa1aa638c421e



### Converting a color between spaces

From Lab:

    selenized/utils$ python convert.py "25,-10,-16"

    CIE L*a*b*    HSV           sRGB      AppleRGB
    -----------   -----------   -------   --------
     25 -10 -16   198  74  33   #154053   #143242

From sRGB (must be given in hex format):

    selenized/utils$ python convert.py "a8bcc3"

    CIE L*a*b*    HSV           sRGB      AppleRGB
    -----------   -----------   -------   --------
     75  -6  -6   196  14  76   #a8bcc3   #99aeb6



### Generating config files from templates

    selenized/utils$ python colorfiller.py itermcolors.template selenized_medium
    Processing itermcolors.template... result written to `itermcolors`.

