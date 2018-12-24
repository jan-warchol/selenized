Features
--------

### Comfortable contrast

A couple years ago I noticed that my eyes quickly grew tired when I was working
in a terminal.  It turned out that the problem was the palette I was using at
that time - it was white text on dark violet background (default Ubuntu
terminal colors - see [example](http://i.imgur.com/wICCS7x.png)).  High
contrast like that tires the eye - that's why professional graphic software
often use gray in their interfaces.

![Selenized contrast sample](http://i.imgur.com/Y11xuwv.png)

Selenized has moderate-to-low contrast - the difference in LAB lightness
between foreground and background is 50, which is exactly half the distance
between pure black and white.  The result is easy on eyes but still very
readable, even on poor displays - see a [side-by-side comparison of Selenized
and Ubuntu palettes](http://i.imgur.com/MtpKFFf.png).

<!-- [selenized manpage example](http://i.imgur.com/twNvCfk.png) -->



### Balanced accent colors

It's not just foreground and background colors that matter. Lightness of all
accent colors need to be carefully adjusted, too: we want them to be equally
readable against the background, but at the same time they cannot have *exactly*
the same lightness because that would make them harder to tell apart (for
example, our eyes expect yellow to be brighter than orange and orange brighter
than red).

<!-- ![Selenized accent colors diagram](http://i.imgur.com/kxylyHe.png) -->

I have fine-tuned the lightnesses to ensure that all colors present an even
contrast, even red and blue (which are too dark in many palettes).  You can
read more about accent color lightness and see a comparison between Selenized
and other palettes [here](balancing-lightness-of-colors.md) (warning: extreme
ugliness of some palette examples may scorch your eyes!).



### Variants for different conditions

Reducing contrast inside terminal window is one thing, but what about the
contrast of the whole desktop?  If you have your terminal side-by-side with a
window that has black text on white background (e.g. a document viewer or a
browser), the resulting contrast between the two windows may make the terminal
less readable.  That's why Selenized dark is has relatively light background:
this ensures better readability and prevents eye fatigue when used next to a
bright/high-contrast window.

![Selenized next to black&white Wikipedia](http://i.imgur.com/OX2Ce2r.png)

There is also a "black" variant meant for people who need higher contrast -
either due to especially bad display/lightness conditions, or because they are
not yet used to low contrast palettes.

