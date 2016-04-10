Selenized color palette
=======================

Selenized is a color palette for terminal emulators. I used
[CIELAB](http://en.wikipedia.org/wiki/Lab_color_space) color space to ensure
balanced contrast and lightness across the whole palette, for great readability
without tiring the eyes. Also, I carefully adjusted accent colors to be both
pleasing and clearly distinguishable (even on poor quality screens).  Selenized
comes in 3 variants (medium, dark and black) so that you can pick the one that
works best in your working environment.

You can read more about the design [here](#features).

_Note: this is work in progress - the colors are expected to change slightly._



Installation
------------

Ready-to-use config files are available for the following terminals:
- [GNOME terminal](gnome-terminal) (default terminal on Ubuntu, Linux Mint and
  other Linux distros using Gnome)
- [Konsole](konsole) (KDE's terminal)
- [Terminator](terminator)
- [urxvt](urxvt)
- [iTerm](iterm)
- if you use Terminal.app (default OS X terminal), I recommend switching to
  [iTerm](iterm), for reasons listed [here](terminal-app).

If your terminal is not listed here, you can always manually copy [hex
values](the-values.md) into its preferences.  Please consider sending me a pull
request with the resulting configuration so that I can add it to officially
supported terminals :-)



Palette variants
----------------

### Selenized medium

![Selenized medium screenshot](http://i.imgur.com/NI8RQaT.png)

Relatively high lightness of this version makes it well suited for using
side-by-side with programs that have black text on white background (e.g. pdf
documents, many websites etc.).


### Selenized dark

![Selenized dark screenshot](http://i.imgur.com/y2dMcsE.png)

It has exactly the same hues and overall contrast as the medium version, just
the lightness is shifted.  It will feel familiar to people used to Solarized
palette.


### Selenized black

Don't like colorful backgrounds and prefer oldschool black-and-white look?  Or
maybe you'd like some more contrast?  Try this variation.

![Selenized black screenshot](http://i.imgur.com/PVKtHEC.png)


### Selenized light

I plan to add a dark-on-light variant when I finish adjusting current ones.



Features
--------

### Comfortable contrast

A couple years ago I noticed that my eyes quickly grew tired when I was working
in a terminal.  It turned out that the problem was the palette I was using at
that time - it was white text on dark violet background (default Ubuntu
terminal colors - see [example](http://i.imgur.com/wICCS7x.png)).  High
contrast like that tires the eye - that's why professional graphic software
often use gray in their interfaces.

![Selenized contrast sample](http://i.imgur.com/SRL3n03.png)

Selenized has moderate-to-low contrast - the difference in LAB lightness
between foreground and background is 50, which is exactly half the distance
between pure black and white.  The result is easy on eyes but still very
readable, even on poor displays - see a [side-by-side comparison of Selenized
and Ubuntu palettes](http://i.imgur.com/Q5ECiYK.png).

<!-- [selenized manpage example](http://i.imgur.com/twNvCfk.png) -->



### Balanced accent colors

It's not just foreground and background colors that matter. Lightness of all
accent colors need to be carefully adjusted, too: we want them to be equally
readable against the background, but at the same time they cannot have *exactly*
the same lightness because that would make them harder to tell apart (for
example, our eyes expect yellow to be brighter than orange and orange brighter
than red).

Selenized keeps the difference in LAB lightness between accent colors and
background above 35, ensuring that all of them are nicely readable - even red
and blue.

![Selenized accent colors example](http://i.imgur.com/kSFGE0R.png)

Many color palettes do this wrong.  For example, rxvt default palette uses
quite bright yellow any cyan, while blue is so dark that it's actually almost
impossible to read against the background.



### Variants for different conditions

Reducing contrast inside terminal window is one thing, but what about the
contrast of the whole desktop?  If you have your terminal side-by-side with a
window that has black text on white background (e.g. a document viewer or a
browser), the resulting contrast between the two windows will make Selenized
dark less readable.  That's why Selenized includes a "medium" variant - it has
exactly the same hues and overall contrast, just the lightness is shifted: this
ensures better readability and prevents eye fatigue when used next to a
bright/high-contrast window.

![Selenized next to black&white Wikipedia](http://i.imgur.com/HUvDnDy.png)

There is also a "black" variant meant for people who need higher contrast -
either due to especially bad display/lightness conditions, or because they are
not yet used to low contrast palettes.



What about _Solarized_?
-----------------------

Selenized is based on Solarized color scheme by Ethan Schoonover (yay, I've
forked a color scheme!).  The name is derived from the greek word 'selene',
which means the moon (as opposed to the sun in solarized).  I really liked the
design principles behind Solarized, but there are a couple issues with it:

- Some accent colors are suboptimal (TODO: add colorwheel image):
  - magenta is easy to confuse with red (TODO: add picture with git log),
  - orange is very easy to confuse with red (note that there is no orange in
    6-color version of selenized - it will be added in 8-color version),
  - green is too close to yellow (I wouldn't actually call it green - in my
    opinion it's more like olive, and I don't like it at all)
  - blue is easy to confuse with violet,
  - cyan and green are not very saturated, which makes it just slightly too
    similar to the foreground color.
- The contrast is slightly wrong:
  - if you have a window with solarized colorscheme side-by-side with another
    window (e.g. browser) that uses black-on-white text (as most of the
    websites do), solarized becomes too hard to read in that context.
    <screenshot with wikipedia page>
  - the dark version is too dark.
  - I know that Ethan says on Solarized website that he tested the scheme on a
    variety of monitors in different lighting conditions, but nevertheless I
    have encountered situations when solarized's legibility was poor due to bad
    display.
- terminals weren't built for 8 accent colors - they were built for 6 colors.
  Solarized tries to implement more colors using some very ugly hacks which
  cause all applications that are not solarized-aware to look weird.
- I think that Ethan's decision to use exactly the same accent colors in both
  light and dark versions of the colorscheme was wrong.  This constraint forces
  the lightness of the accent colors to be a compromise, rather than picking
  optimal lightness for dark and light versions separately - and the benefits
  of this solution are, in my opinion, negligible.



Contributing
------------

I'm happy to add support for more terminal emulators and command-line
applications - please open pull requests :-)

Also, let me know if you'd like to help with developing extended version of
Selenized (with 8 accent colors), or if you encountered a situation where some
colors were difficult to read.  As long as Selenized is in beta phase I'll
consider adjusting the colors.



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

