Selenized color palette for xterm
=================================

Installation
------------

save the file with the palette somewhere and add an include statement like this
to your `~/.Xdefaults`:

    #include "<path to palette file>"

(note the double quotes around the path).  After that, run the following command:

    xrdb -merge ~/.Xdefaults

