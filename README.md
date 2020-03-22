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

Ready-to-use config files are available for the following:

### Terminal Emulators

- [Alacritty](alacritty)
- [Blink](blinksh) mobile shell for iOS
- [Gnome terminal](gnome-terminal) (default terminal on Ubuntu, Mint and other Gnome-based distros)
- [Guake](guake)
- [iTerm](iterm)
- [Kitty](kitty)
- [Konsole](konsole) (default KDE terminal)
- [Mintty](mintty)
- [Terminal.app](terminal-app) (default OS X terminal)
- [Terminator](terminator)
- [Termite](termite)
- [Tilda](tilda)
- [Tilix](tilix)
- [urxvt](urxvt)
- [xterm](xterm)

### Editors & IDEs

- [Vim](vim)
- [VS Code](visual-studio-code)

Support for more editors is planned as soon as highlighting rules settle down
(see issues #67, #68, #69).

### Other applications

- [Dircolors](dircolors) (file coloring rules for CLI utilities like `ls`)
- [i3](i3) window manager and status line
- [Manpage coloring](selenized-man)
- [Midnight Commander](mc) skin
- [Rofi](rofi) window switcher
- [Slack](slack) sidebar theme
- [Wofi](wofi) (wayland replacement for Rofi)

### Manual installation

If your application is not listed above, you can manually copy [hex
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

Oldschool black-and-white look with a little more contrast.



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
