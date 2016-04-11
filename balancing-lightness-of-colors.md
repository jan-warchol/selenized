Balancing lightness of accent colors
------------------------------------

Desiginig a readable and good-looking color palette requires carefully
adjusting the lightness of all colors so that they present an even contrast
against the background.  This is quite tricky and many palettes do it wrong -
below you can see some examples that will help you understand the problem.
Selenized keeps the difference in LAB lightness between accent colors and
background above 33, ensuring that all of them are nicely readable, and keeps
the difference between darkest and brightest colors below 20, ensuring that
they look consistent with each other.

_**Note:** keep in mind that the display used to view these examples matters a
lot.  For example, my laptop has a poor screen with washed-out colors, and the
examples I describe as "lurid" do not look that bad on it - but when I view
them on a good external monitor with full sRGB gamut, my eyes scream and want
to fall out._



Examination of various palettes
-------------------------------

### Xterm

![Accent colors example - xterm](http://i.imgur.com/E0yIUFv.png)

I think this may be the worst palette I ever saw.  It is both ugly and
unreadable:
- accent colors are too saturated which makes the whole palette lurid and
  aggressive,
- blue is too dark - really hard to read against black background,
- foreground color is too bright compared to the accent colors.



### Linux console

![Accent colors example - linux console](http://i.imgur.com/bq3C487.png)

This palette is *slightly* less lurid, but it manages to make blue even darker
and less readable than xterm.



### Rxvt

![Accent colors example - rxvt](http://i.imgur.com/bCJWGVr.png)

Black-on-white palettes, like this one, can have similar problems - just with
different colors: in this case green, cyan and (especially) yellow are too
bright.  Can you see all the yellow-colored punctuation here?  Me neither.  Of
course, this palette also has too much overall contrast - pure black foreground
on pure white background is guaranteed to tire your eyes in the long run.



### Linux Mint

![Accent colors example - linux mint](http://i.imgur.com/NdGbiHg.png)

Default palette of Linux Mint is an example where lightness of accent colors as
a group is completely off.  Here, background lightness is 27, foreground
lightness 100, while accent colors are between 39 (violet) and 68 (yellow) -
way too close to the background and too far from foreground.



### Ubuntu

![Accent colors example - ubuntu](http://i.imgur.com/WkYpoie.png)

Similarly to Linux Mint palette, accent colors are much too dark compared to
bright white foreground.  The only slight improvement is in the contrast
between accent colors and background - but the result is far from perfect:
violet is still not readable enough against dark violet background.



### Ancient Selenized

![Accent colors example - ancient selenized](http://i.imgur.com/FJ7vgQT.png)

I also made some mistakes in palette design.  Here is a very old version of
Selenized, not free from issues.  Overall contrast here is too low - in
particular red is too dark.  Apart from that, some colors (notably red and
magenta) are too saturated, and the effect is that the palette is a bit lurid.



### Terminator

![Accent colors example - terminator](http://i.imgur.com/ya6vZrn.png)

This one is significantly better than the previous ones, but blue and violet
are still too dark.  If they were slightly lighter it would be quite decent.



### Current Selenized

![Accent colors example - current selenized](http://i.imgur.com/4b5Z1be.png)

And here comes selenized ("black" variant).  Notice how all accent colors, as
well as foreground, are clearly readable against the background.



Why so many palettes get this wrong?
------------------------------------

Since correct lightness is so important for readability of a palette, why there
are so many problems with it?  I think there are two reasons.

First, meaningfully comparing lightness of colors requires using special tools.
You cannot compare lightness of two colors using their RGB coordinates.
HSV/HSB and HSL may appear to be the solution, but unfortunately they will not
produce correct results, because they are not perceptually uniform.  One has to
use color space like CIE Lab to get correct lightness relationships - you can
read more about this
[here](https://vis4.net/blog/posts/avoid-equidistant-hsv-colors/).

Second, there is some legacy involved.  Many of the old color palettes used to
have uneven color lightness and some programs designed their color settings to
match these old palettes - for example, see an issue I had with [Midnight
Commander](https://github.com/janek-warchol/selenized/issues/7).  This makes
designing universal color palettes harder.

