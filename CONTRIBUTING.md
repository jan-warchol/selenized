Syntax highlighting design principles
-------------------------------------

Here are some general guidelines for deciding which types of tokens should be
colored with which color:

- overall effect shouldn't be overwhelming - don't color everything, strive for
  harmony (compare with [this monokai
  example](https://i.imgur.com/ATVTHr6.png), which has colors all over the
  place)
- contrasting colors shouldn't appear next to each other too often
- structurally most important elements should be most visible
- less important content should be visually "in the background"
- short tokens (and punctuation, if it's to be colored) should preferably use
  stronger colors 
- long tokens should use "softer" colors to avoid making the result too
  aggressive
- rare tokens should use a color that draws attention and is not used by some
  common tokens
- try to leverage common color associations wherever possible (e.g. red ->
  problem, green -> no problem)
- warm colors (orange, yellow) are best for tokens associated with action
- cold colors (cyan, blue) are best for things that don't change
- [non-spectral colors](https://en.wikipedia.org/wiki/Spectral_color) (purple,
  magenta) are best for things with special meaning/behavior

This means that, for example:

- comments must be gray, so that they fade into background (unlike many schemes
  in which comments are green and clutter the view)
- function and class definitions must be clearly visible from distance (perhaps
  bright bold foreground)
- orange is a good color for numbers
- exceptions should probably be bold and they must not be green
- preprocessor, interpolation, macros and other meta-processing things "feel"
  magenta
- cyan is a good color for `CONSTANTS`
- should boilerplate be blue? or gray? or not colored at all?


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

