Selenized color scheme
----------------------

This color scheme is inspired by Solarized color scheme by Ethan Schoonover (yay,
I've forked a color scheme!).  The name is derived from the greek word 'selene',
which means the moon (as opposed to the sun in solarized).

What's wrong with solarized?
- the dark version is too dark
- cyan is not saturated enough, it blends with the foreground color
- red is too similar to orange
- violet is too similar to blue
- green looks very yellowish
- terminals weren't built for 8 colors - they were built for 6 colors with bright versions.
- solarized generally tries to do too much with too little.  E.g. by enforcing an arbitrary
constraint (that the same accent colors must be used in light and dark versions) Ethan was
forced to make both versions non-optimal.

This is a color scheme I use with my terminal.  It has moderate brightness and
medium foreground/background contrast to reduce eye strain, but at the same
time it uses quite saturated colors with contrasting hues for unambiguous 
syntax highlighting.

This is very much work in progress.  Expect the colors to change (albeit not
very much); I also plan to add a dark-on-light version and configuration files
for other terminal emulators (and possibly also other programs).


Notes
-----

The point is not to have accent colors with identically the same lightness,
because that would look strange and some colors would be hard to distinguish
(for example, our eyes expect yellow to be brighter than orange and orange
brighter than red).  Ethan does make some leeway here, but he stops short of
the goal of unambiguous colors (because he's limited by the design decision
to use exactly the same accent colors in light and dark versions of the scheme).
