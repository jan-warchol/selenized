Selenized color palette
=======================

Selenized is a color theme for terminals and text editors, carefully designed
using professional-grade [CIE
L*a*b*](http://en.wikipedia.org/wiki/Lab_color_space) color space for maximum
readability and great eye comfort.


Design principles
-----------------

- make the contrast just right: strong but not tiring to the eyes
- adjust lightness of all colors for uniform readability
- select colors in a way that boosts code comprehension
- make it as beautiful and visually pleasing as possible

Read more about the design [here](features-and-design.md).



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
- [Tilix](tilix)
- [Alacritty](alacritty)
- [mintty](mintty)

If your terminal is not listed here, you can always manually copy [hex
values](the-values.md) into its preferences.  Please consider sending me a pull
request with the resulting configuration so that I can add it to officially
supported terminals :-)



Palette variants
----------------

### Selenized dark

![Selenized dark screenshot](http://i.imgur.com/yM0vadH.png)

Like _Solarized dark_, but better.



### Selenized black

![Selenized black screenshot](http://i.imgur.com/rXIH87x.png)

Oldschool black-and-white look with a littel more contrast.



### Selenized light

![Selenized light screenshot](http://i.imgur.com/kQVgD5U.png)

A warm sepia variant, corresponding to _Solarized light_.



### Selenized white

![Selenized white screenshot](http://i.imgur.com/sc0Uv9h.png)

Unlike many dark-on-white palettes, yellow color is readable here.



What about _Solarized_?
-----------------------

There is a popular color palette named _Solarized_. I really liked the design
principles behind Solarized, but it has a couple issues, which [Selenized
solves](whats-wrong-with-solarized.md).

By the way, the name is derived from the greek word "selene", which means
the moon (as opposed to the sun in Solarized).



Known issues
------------

Some command-line programs need reconfiguration to look good with Selenized,
because they make assumptions about the colors configured in terminal (see
[this issue](https://github.com/janek-warchol/selenized/issues/7) for details):

- [`ls`](dircolors/)
- [Midnight Commander](mc/)



Contributing and development
----------------------------

See [`CONTRIBUTING.md`](CONTRIBUTING.md).
