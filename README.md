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

![Selenized dark screenshot](http://i.imgur.com/fhYxsbD.png)

| Color          | sRGB/hex  | CIELab       |
| -------------- | --------- | ------------ |
| background     | `#07293b` | `15 -07 -15` |
| foreground     | `#90a0ae` | `65 -04 -09` |
| black          | `#213f52` | `25 -07 -15` |
| red            | `#dd3031` | `50  66  44` |
| green          | `#559f1e` | `59 -40  54` |
| yellow         | `#ba9610` | `64  06  65` |
| blue           | `#2d7bdf` | `51  04 -59` |
| magenta        | `#c455d5` | `55  58 -46` |
| cyan           | `#12ab9e` | `63 -40 -04` |
| white          | `#90a0ae` | `65 -04 -09` |
| bright black   | `#5d7b90` | `50 -07 -15` |
| bright red     | `#ed413d` | `55  66  44` |
| bright green   | `#63ad2d` | `64 -40  54` |
| bright yellow  | `#c9a323` | `69  06  65` |
| bright blue    | `#4188ee` | `56  04 -59` |
| bright magenta | `#d363e3` | `60  58 -46` |
| bright cyan    | `#2db9ab` | `68 -40 -04` |
| bright white   | `#aabbc9` | `75 -04 -09` |



Selenized medium
----------------

Sometimes the dark version is a bit too dark when used side-by-side with some
other program that has black text on white background.  In these situations
medium version comes handy (it has exactly the same hues and overall contrast,
just the lightness is shifted).

![Selenized medium screenshot](http://i.imgur.com/5qpQRPe.png)

| Color          | sRGB/hex  | CIELab       |
| -------------- | --------- | ------------ |
| background     | `#27465a` | `28 -07 -16` |
| foreground     | `#b2c4d1` | `78 -04 -09` |
| black          | `#3f5e73` | `38 -07 -16` |
| red            | `#ff594f` | `63  66  44` |
| green          | `#79c344` | `72 -40  54` |
| yellow         | `#e1b83c` | `77  06  65` |
| blue           | `#5d9cff` | `64  04 -59` |
| magenta        | `#ea79fb` | `68  58 -46` |
| cyan           | `#4cd0c1` | `76 -40 -04` |
| white          | `#b2c4d1` | `78 -04 -09` |
| bright black   | `#7e9db5` | `63 -07 -16` |
| bright red     | `#ff685b` | `68  66  44` |
| bright green   | `#87d151` | `77 -40  54` |
| bright yellow  | `#f0c64a` | `82  06  65` |
| bright blue    | `#6daaff` | `69  04 -59` |
| bright magenta | `#f987ff` | `73  58 -46` |
| bright cyan    | `#5cdecf` | `81 -40 -04` |
| bright white   | `#c0d1df` | `83 -04 -09` |



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

