How Selenized improves upon Solarized
=====================================

Selenized is based on [Solarized color
palette](http://ethanschoonover.com/solarized), which was designed by Ethan
Schoonover.  Solarized has some great features, but it does have a few issues
as well (this is why I have created Selenized) - they are discussed below.



Problems with accent colors
---------------------------

<!-- TODO: add colorwheel image -->

Some accent colors in Solarized are a bit too similar to each other.
For example, magenta can be easy to confuse with red on some displays and in
some situations.  Yes, they *are* different, but they should be less ambiguous.
Similarly, green is too close to yellow.

<!-- TODO: add picture with git log -->

In fact, green in Solarized is not like typical green - it is more like olive.
Personally I prefer more "traditional" green.

Selenized uses different, less ambiguous hues than Solarized (although the
difference may seem small, especially on cheap displays).



Problems with contrast
----------------------

Ethan says on Solarized website that he had tested Solarized on a variety of
monitors in different lighting conditions.  However, I have encountered
situations when readability of Solarized was not satisfactory - especially on
mediocre displays (maybe Ethan only used high-quality screens for testing?).
Selenized has slightly increased contrast (50 "Lab units" instead of 45) and
looks good on all displays, expensive and cheap.

Another, more serious problem is that Solarized dark works well when used all
by itself, but it is too dark to be placed next to a high-contrast window that
has black text on white background (e.g. a pdf or a browser).  Here is a
screenshot of Solarized dark next to Wikipedia:

![Solarized next to black&white Wikipedia](http://i.imgur.com/UlOxerG.png)

This problem is more visible when someone uses Solarized dark for snippets of
code on a high-contrast website, like this:

![short code sample with Solarized](http://i.imgur.com/vStjfca.png)

Selenized solves this problem by increasing contrast and making the whole dark
variant lighter:

![Selenized next to black&white Wikipedia](http://i.imgur.com/OX2Ce2r.png)

![short code sample with Selenized](http://i.imgur.com/fm8Orae.png)



Problems with implementation
----------------------------

One of the features of Solarized is that both light and dark variants can be
constructed from the same set of 16 colors.  This is a nice property, but
implementing it in case of terminal emulators requires using a weird mapping of
color codes to actual color values.

![color code assignment - solarized](http://i.imgur.com/Rn3yhw1.png)

For example, you can see that color code traditionally used for bright/bold
green is used by Solarized for "secondary content" (i.e. color used for
comments), and so on. The result is that many command line programs will
produce weird-looking or unreadable output unless they are configured with
specific Solarized settings.  See [this
issue](https://github.com/altercation/solarized/issues/220) and [this Stack
Overflow
question](http://stackoverflow.com/questions/14093554/vim-solarized-on-os-x-terminal-app-incorrect-colors)
for an example.

Selenized adheres to standard meanings of terminal color codes:

![color code assignment - selenized](http://i.imgur.com/h6Rog02.png)

Some programs may need adjustments to work well with Selenized, but such issues
happen less frequently.

Apart from terminals, I think that the decision to use exactly the same accent
colors in both light and dark variants of Solarized was wrong.  This constraint
forces the lightness of the accent colors to be a compromise, rather than
picking optimal lightness for dark and light versions separately - and the
benefits of this solution are, in my opinion, negligible.

