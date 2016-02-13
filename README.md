Selenized color palette
=======================

Selenized is a color palette for terminal emulators.  It is designed to be easy
on eyes (by reducing foreground/background contrast) while retaining reasonably
strong - yet balanced - accent colors.

Note that currently Selenized defines 6 accent colors and 5 monotones, because
that's the standard in terminal emulators.  I plan to add an expanded version
with 8 or 9 accent colors later.  Keep in mind that this is work in progress -
the colors are expected to change slightly.



Selenized dark
--------------

![Selenized dark screenshot](http://i.imgur.com/dlKkhXM.png)

| Color          | Value     |
| -------------- | --------- |
| background     | `#04293b` |
| foreground     | `#8fa0ae` |
| black          | `#2e3d49` |
| red            | `#dc3840` |
| yellow         | `#be9600` |
| green          | `#3fa000` |
| cyan           | `#00afa1` |
| blue           | `#0777da` |
| magenta        | `#db49da` |
| white          | `#8fa0ae` |
| bright black   | `#2e3d49` |
| bright red     | `#dc3840` |
| bright yellow  | `#be9600` |
| bright green   | `#3fa000` |
| bright cyan    | `#00afa1` |
| bright blue    | `#0777da` |
| bright magenta | `#db49da` |
| bright white   | `#8fa0ae` |



Selenized medium
----------------

Sometimes the dark version is a bit too dark when used side-by-side with some
other program that has black text on white background.  In these situations
medium version comes handy (it has exactly the same hues and overall contrast,
just the lightness is shifted).

![Selenized medium screenshot](http://i.imgur.com/vjKW18k.png)

| Color          | Value     |
| -------------- | --------- |
| background     | `#274559` |
| foreground     | `#b2c3d1` |
| black          | `#4c5c68` |
| red            | `#ff5a5a` |
| yellow         | `#e6b91d` |
| green          | `#67c315` |
| cyan           | `#2dd4c4` |
| blue           | `#4e97ff` |
| magenta        | `#ff6fff` |
| white          | `#b2c3d1` |
| bright black   | `#4c5c68` |
| bright red     | `#ff5a5a` |
| bright yellow  | `#e6b91d` |
| bright green   | `#67c315` |
| bright cyan    | `#2dd4c4` |
| bright blue    | `#4e97ff` |
| bright magenta | `#ff6fff` |
| bright white   | `#b2c3d1` |



Selenized light
---------------

I plan to add a dark-on-light variant when I finish adjusting current ones.



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
  - I know that Ethan says on Solarized website that he tested the scheme on a
    variety of monitors in different lighting conditions, but nevertheless I
    have encountered situations when solarized's legibility was poor due to bad
    display.
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

