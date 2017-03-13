Selenized color palette
=======================

Selenized is a color palette for terminal emulators. I used
[CIELAB](http://en.wikipedia.org/wiki/Lab_color_space) color space to ensure
balanced contrast and lightness across the whole palette, for great readability
without tiring the eyes. Also, I carefully adjusted accent colors to be both
pleasing and clearly distinguishable (even on poor quality screens).  Selenized
comes in 2 variants (dark and black) so that you can pick the one that
works best in your working environment.

You can read more about the design [here](#features).



Installation
------------

Ready-to-use config files are available for the following terminals:
- [GNOME terminal](gnome-terminal) (default terminal on Ubuntu, Linux Mint and
  other Linux distros using Gnome)
- [Konsole](konsole) (KDE's terminal)
- [Terminator](terminator)
- [Guake](guake)
- [urxvt](urxvt)
- [xterm](xterm)
- [iTerm](iterm)
- if you use Terminal.app (default OS X terminal), I recommend switching to
  [iTerm](iterm), for reasons listed [here](terminal-app).

If your terminal is not listed here, you can always manually copy [hex
values](the-values.md) into its preferences.  Please consider sending me a pull
request with the resulting configuration so that I can add it to officially
supported terminals :-)



Palette variants
----------------

### Selenized dark

![Selenized dark screenshot](http://i.imgur.com/yM0vadH.png)

Relatively high lightness of this version makes it well suited for using
side-by-side with programs that have black text on white background (e.g. pdf
documents, many websites etc.).



### Selenized black

Don't like colorful backgrounds and prefer oldschool black-and-white look?  Or
maybe you'd like some more contrast?  Try this variation.

![Selenized black screenshot](http://i.imgur.com/rXIH87x.png)



### Selenized light

A warm sepia variant. This one works wery well especially when you have a lot
of other bright windows opened.

![Selenized light screenshot](http://i.imgur.com/kQVgD5U.png)



### Selenized white

Finally, a white version for completeness. Unlike many white-backgrounded
palettes, all accent colors are well readable here.

![Selenized white screenshot](http://i.imgur.com/sc0Uv9h.png)



Features
--------

### Comfortable contrast

A couple years ago I noticed that my eyes quickly grew tired when I was working
in a terminal.  It turned out that the problem was the palette I was using at
that time - it was white text on dark violet background (default Ubuntu
terminal colors - see [example](http://i.imgur.com/wICCS7x.png)).  High
contrast like that tires the eye - that's why professional graphic software
often use gray in their interfaces.

![Selenized contrast sample](http://i.imgur.com/Y11xuwv.png)

Selenized has moderate-to-low contrast - the difference in LAB lightness
between foreground and background is 50, which is exactly half the distance
between pure black and white.  The result is easy on eyes but still very
readable, even on poor displays - see a [side-by-side comparison of Selenized
and Ubuntu palettes](http://i.imgur.com/MtpKFFf.png).

<!-- [selenized manpage example](http://i.imgur.com/twNvCfk.png) -->



### Balanced accent colors

It's not just foreground and background colors that matter. Lightness of all
accent colors need to be carefully adjusted, too: we want them to be equally
readable against the background, but at the same time they cannot have *exactly*
the same lightness because that would make them harder to tell apart (for
example, our eyes expect yellow to be brighter than orange and orange brighter
than red).

<!-- ![Selenized accent colors diagram](http://i.imgur.com/kxylyHe.png) -->

I have fine-tuned the lightnesses to ensure that all colors present an even
contrast, even red and blue (which are too dark in many palettes).  You can
read more about accent color lightness and see a comparison between Selenized
and other palettes [here](balancing-lightness-of-colors.md) (warning: extreme
ugliness of some palette examples may scorch your eyes!).



### Variants for different conditions

Reducing contrast inside terminal window is one thing, but what about the
contrast of the whole desktop?  If you have your terminal side-by-side with a
window that has black text on white background (e.g. a document viewer or a
browser), the resulting contrast between the two windows may make the terminal
less readable.  That's why Selenized dark is has relatively light background:
this ensures better readability and prevents eye fatigue when used next to a
bright/high-contrast window.

![Selenized next to black&white Wikipedia](http://i.imgur.com/OX2Ce2r.png)

There is also a "black" variant meant for people who need higher contrast -
either due to especially bad display/lightness conditions, or because they are
not yet used to low contrast palettes.



What about _Solarized_?
-----------------------

Selenized is based on color palette called _Solarized_ (yay, I have forked a
color scheme!).  The name is derived from the greek word 'selene', which means
the moon (as opposed to the sun in Solarized).  I really liked the design
principles behind Solarized, but there are a couple issues with it (which
Selenized aims to solve).  You can read more about the differences
[here](whats-wrong-with-solarized.md).



FAQ
---

#### Program X doesn't look good when I use Selenized in my terminal.

Some command-line programs make assumptions about the colors set in the
terminal - for example, they may assume that some color will work well as the
background color.  Using them in a terminal that uses Selenized palette may
require adjusting their color settings - for an example, see [this
issue](https://github.com/janek-warchol/selenized/issues/7) about using
Selenized with [Midnight
Commander](https://github.com/janek-warchol/selenized/tree/master/mc).

Programs with dedicated Selenized skins/configs:

- [`ls`](dircolors/)
- [Midnight Commander](mc/)


#### Where are orange and violet?

Selenized [defines](the-values.md) 8 accent colors: red, orange, yellow, green,
cyan, blue, violet and magenta. However, terminal emulators traditionally have
escape codes for 6 colors (red, yellow, green, cyan, blue and magenta), with
two additional codes for black and white. Therefore, terminal configs included
in this repository don't include orange and violet. However, configs for GUI
programs will include the full palette (as GUI programs can define as many
colors as they want).



Development & Contributing
--------------------------

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


