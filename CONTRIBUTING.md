Where are orange and violet?
----------------------------

Selenized [defines](the-values.md) 8 accent colors: red, orange, yellow, green,
cyan, blue, violet and magenta. However, terminal emulators traditionally have
escape codes for 6 colors (red, yellow, green, cyan, blue and magenta), with
two additional codes for black and white. Therefore, terminal configs included
in this repository don't include orange and violet. However, configs for GUI
programs will include the full palette (as GUI programs can define as many
colors as they want).



Development
-----------

Selenized is still work-in-progress.  Here are some of my plans for the future:
- add ready-to-use config files for more terminals
- support more command-line programs (add selenized skins/configs for them - in
  particular I'd like to fine-tune dircolors to look as good as possible with
  Selenized)
- add a dark-on-light variant of the palette
- extend Selenized to 8 accent colors (add orange and violet, like in
  Solarized)
- add color schemes for popular IDEs
- add a script that would allow [adjusting Selenized to your taste](#forking)
  using a web interface
- maybe even create a library that would allow adjusting LAB lightness in
  arbitrary color palettes based on the experience I got creating Selenized
- research perceptually uniform color spaces - maybe they could be used to
  improve consistency of Selenized colors even further?  See
  [here](www.brucelindbloom.com/UPLab.html) and
  [here](https://en.wikipedia.org/wiki/Munsell_color_system).

If you'd like to help with any of these, please get in touch - open a pull
request or contact me at jan.warchol@gmail.com.

Also, open an issue if you found a program that doesn't look good with
Selenized terminal or encountered a situation where Selenized was not readable
enough.  Until version 1.0 I'm open to suggestions on adjusting the colors.



Forking
-------

You are welcome to adjust Selenized to your taste - I can imagine that some
people may want to change the hue of the background/content colors or adjust
the contrast slightly.  When doing so, please keep in mind the following
(especially if you'd like to publish your fork and use "Selenized" in its
name):
- always use CIELAB color space to check lightness of the resulting colors.
  You don't need Photoshop for this - there are online tools for CIELAB-sRGB
  conversion (although they may produce slightly different results than
  Photoshop).
- keep overall contrast (i.e. difference in CIELAB lightness between foreground
  and background colors) between 45 and 65 units.  Anything outside this range
  is really not good.
- keep accent color contrast (i.e. difference in CIELAB lightness between
  accent color and background) above 30 units. This really is the minimum.
- preferably don't change accent color hues and their relative lightness at
  all.

