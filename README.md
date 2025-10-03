Selenized color palette
=======================

<!--
Solarized redesigned: fine-tuned color palette for programmers with focus on readability.
-->

![Selenized dark screenshot](http://i.imgur.com/yM0vadH.png)

After researching perceptually uniform color spaces, _4 years of testing_,
refining hues and fine-tuning lightness using professional grade [CIE
Lab](http://en.wikipedia.org/wiki/Lab_color_space) color space, the task of
redesigning venerable Solarized is almost finished!
Results:

* Easy on the eyes.
* **Beautiful**, vibrant and easily **distinguishable** accent colors.
* **Great readability** and better compatibility with Web Content
  [Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/).

Read more [about the design](features-and-design.md)
and see how it [improves on Solarized](whats-wrong-with-solarized.md).



Installation
------------

Ready-to-use config files are available for the following:

### Terminal Emulators

- [Alacritty](terminals/alacritty)
- [Blink](terminals/blinksh) mobile shell for iOS
- [Gnome terminal](terminals/gnome-terminal) (default terminal on Ubuntu, Mint and other Gnome-based distros)
- [Guake](terminals/guake)
- [iTerm](terminals/iterm)
- [Kitty](terminals/kitty)
- [Konsole](terminals/konsole) (default KDE terminal)
- [Mintty](terminals/mintty)
- [Terminal.app](terminals/terminal-app) (default OS X terminal)
- [Terminator](terminals/terminator)
- [Termite](terminals/termite)
- [Tilda](terminals/tilda)
- [Tilix](terminals/tilix)
- [urxvt](terminals/urxvt)
- [Windows Terminal](terminals/windows-terminal)
- [xterm](terminals/xterm)

### Editors & IDEs (help wanted!)

- [Vim](editors/vim)
- [VS Code](editors/visual-studio-code)

🔥 **I need your opinion!** 🔥 There are some design decisions that need to be made
before adding support for more editors. Your feedback would be very helpful -
please comment on
[issue 68](https://github.com/jan-warchol/selenized/issues/68) and
[issue 74](https://github.com/jan-warchol/selenized/issues/74).


### Other applications

- [Dircolors](other-apps/dircolors) (file coloring rules for CLI utilities like `ls`)
- [i3](other-apps/i3) window manager and status line
- [Manpage coloring](other-apps/selenized-man)
- [Midnight Commander](other-apps/mc) skin
- [Rofi](other-apps/rofi) window switcher
- [Slack](other-apps/slack) sidebar theme
- [Wofi](other-apps/wofi) (wayland replacement for Rofi)

### Manual installation

If your application is not listed above, it's easy to set the colors manually.
See [this document](manual-installation.md) for guidelines.





Compatibility notes
-------------------

Some command-line programs may need reconfiguration to look good with Selenized,
because they make assumptions about the colors configured in terminal (see
[this issue](https://github.com/janek-warchol/selenized/issues/7) for details):

- [`ls`](dircolors/)
- [Midnight Commander](mc/)

However, this is quite rare; vast majority of software works great
out-of-the-box.



Contributing and development
----------------------------

See [`CONTRIBUTING.md`](CONTRIBUTING.md).



About the name
--------------

The name of the project is derived from the greek word "selene", which means
_the moon_ - as opposed to _the sun_ in Solarized.

