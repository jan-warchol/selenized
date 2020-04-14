Features
--------

### Comfortable contrast

It all started when I noticed that my eyes were quickly growing tired when
coding.  I had been using default Ubuntu colors back then (white on dark
magenta), and the contrast was simply _too high_.

![Selenized contrast sample](http://i.imgur.com/Y11xuwv.png)

Selenized has moderately low contrast - a bit more than half the distance
between pure black and white.  The result is easy on the eyes, but still **very
readable:** long coding sessions are not a strain anymore!  ([compare with
Ubuntu colors here](http://i.imgur.com/MtpKFFf.png))

<!-- [selenized manpage example](http://i.imgur.com/twNvCfk.png) -->



### Balanced and beautiful accent colors

Lightness of accent colors needs to be carefully adjusted, so that they are
both pleasant and present an even contrast against the background. This is
tricky because of things like [Helmholtz–Kohlrausch
effect](https://en.wikipedia.org/wiki/Helmholtz%E2%80%93Kohlrausch_effect) and
eye cone sensitivity differences.

![Selenized accent colors diagram](http://i.imgur.com/QNKIw1U.png)

Selenized harmonizes the lightnesses while preserving each color's
individuality (e.g. yellow should be brighter than red). This is possible
thanks to the use of perceptually uniform CIE Lab color space.

![Accent colors in xterm and ubuntu](http://i.imgur.com/wNCz40F.png)

Many palettes - including default coloring in xterm, Ubuntu terminal and
Sublime Text - [weren't designed this
way](https://vis4.net/blog/posts/avoid-equidistant-hsv-colors/): they have a
lot of variation in lightness. You can see above how this leads to bad
readability.



### Variants for different needs

Selenized includes four variants so that everyone will find something that
suits their taste. Thanks to the magic of CIE Lab color space, all variants
share the same lightness relationships, resulting in exactly the same
readability.


#### Selenized dark & light

![Selenized dark screenshot](http://i.imgur.com/yM0vadH.png)
![Selenized light screenshot](http://i.imgur.com/kQVgD5U.png)

Like _Solarized_, but better. Dark teal and warm sepia complement each other nicely.


#### Selenized black & white

Contrast inside terminal/editor is one thing, but what about the whole desktop?
A window with black text on white background (e.g. a pdf document) next to your
code will influence its perceived brightness. Also, what if you are working
outdoors?

![Selenized black screenshot](http://i.imgur.com/rXIH87x.png)
![Selenized white screenshot](http://i.imgur.com/sc0Uv9h.png)

That's why selenized has black and white variants: oldschool look with a little
more contrast. Notice that yellow color on white background is readable here.

