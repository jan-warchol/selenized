Contributing to Selenized
=========================

Development roadmap
-------------------

Selenized is quite complete, but there are some things that could still be done.
Some ideas for the future:

- better, more nuanced syntax highlighting rules (see [issue
  68](https://github.com/jan-warchol/selenized/issues/68))
- web interface for [adjusting Selenized to your taste](#forking)
- a library that would allow "fixing" existing color palettes (by adjusting Lab
  lightness of their colors while keeping original hue and saturation)
- learn more about perceptually uniform color spaces - maybe they could be used
  to improve consistency of Selenized colors even further? See
  [here](www.brucelindbloom.com/UPLab.html) and
  [here](https://en.wikipedia.org/wiki/Munsell_color_system).

And of course, adding support for more programs, terminals, editors, IDEs etc.

If you'd like to help but are not sure where to start, contact me at
jan.warchol@gmail.com. Also, please [open an
issue](https://github.com/jan-warchol/selenized/issues) if you found a program
that doesn't look good with Selenized colors in your terminal.



Customization
-------------

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

