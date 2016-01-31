Selenized color scheme
----------------------

![Screenshot of selenized](http://i.imgur.com/08cgQrD.jpg)

This is a color scheme I use with my terminal.  It has moderate brightness and
medium foreground/background contrast to reduce eye strain, but at the same
time it uses quite saturated colors with contrasting hues for unambiguous 
syntax highlighting.

This is work in progress; expect the colors to change slightly. I also plan to
add a dark-on-light version and configuration files for other terminal
emulators (and possibly also other programs).



The colors
----------

Here are HEX values for Selenized 6-colors.  I plan to add 8-color version
later.

| Color | Selenized | Selenized dark | Selenized steel |
| ----- | --------- | -------------- | --------------- |
| foreground | `#b2c3d1` | `#8fa0ae` | `#c1c1c1` |
| background | `#274559` | `#04293b` | `#424242` |
| red        | `#ff5a5a` | `#dc3840` | `#ff5a5a` |
| green      | `#67c315` | `#3fa000` | `#67c315` |
| yellow     | `#e6b91d` | `#be9600` | `#e6b91d` |
| blue       | `#4e97ff` | `#0777da` | `#4e97ff` |
| violet     | `#ff6fff` | `#db49da` | `#ff6fff` |
| cyan       | `#2dd4c4` | `#00afa1` | `#2dd4c4` |
| black      | `#4c5c68` | `#2e3d49` | `#595959` |



Selenized? Did you mean "Solarized", maybe?
-------------------------------------------

This color scheme is inspired by Solarized color scheme by Ethan Schoonover (yay,
I've forked a color scheme!).  The name is derived from the greek word 'selene',
which means the moon (as opposed to the sun in solarized).  I really liked the
design principles behind Solarized, but there are a couple issues with it:

- Some accent colors are suboptimal:
  - orange is very easy to confuse with red (note that there is no orange in
    6-color version of selenized - it will be added in 8-color version),
  - green is too close to yellow (I wouldn't actually call it green - in my
    opinion it's more like olive, and I don't like it at all)
  - blue is easy to confuse with violet,
  - cyan is not very saturated, which makes it just slightly too similar to the
    foreground color.
- The contrast is slightly wrong:
  - if you have a window with solarized colorscheme side-by-side with another
    window (e.g. browser) that uses black-on-white text (as most of the
    websites do), solarized becomes too hard to read in that context.
  - the dark version is too dark.
- terminals weren't built for 8 colors - they were built for 6 colors.
  Solarized tries to implement more colors using some very ugly hacks which
  cause all applications that are not solarized-aware to look weird.
- I think that Ethan's decision to use exactly the same accent colors in both
  light and dark versions of the colorscheme was wrong.  This constraint forces
  the lightness of the accent colors to be a compromise, rather than picking
  optimal lightness for dark and light versions separately - and the benefits
  of this solution are, in my opinion, negligible.



Design principles
-----------------

- easy on eyes
- even contrast
- completely unambiguous accent colors 
- as good looking as possible considering other constraints
- straightforward to implement



Notes
-----

The point is not to have accent colors with identically the same lightness,
because that would look strange and some colors would be hard to distinguish
(for example, our eyes expect yellow to be brighter than orange and orange
brighter than red).  Ethan does make some leeway here, but he stops short of
the goal of unambiguous colors (because he's limited by the design decision
to use exactly the same accent colors in light and dark versions of the scheme).

