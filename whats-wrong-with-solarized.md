How Selenized improves on Solarized
===================================

I really liked the design principles behind Solarized - it has some great
features. However, it has a few problems as well, which Selenized solves:

* [Confusing accent colors](#better-accent-colors)
* [Not enough contrast](#slightly-higher-contrast)
* [Dark version is too dark](#better-lightness)
* [Hacky implementation in terminals](#better-terminal-compatibility)



Better accent colors
--------------------

Some accent colors in Solarized are confusing or too similar to each other:

* green is too much like yellow (looks like olive)
* orange looks almost like red
* magenta too close to red as well
* violet is easy to confuse with blue

![Solarized and Selenized colorwheel comparison](https://i.imgur.com/1AsC3pS.png)

This is less of a problem on high-end, color-calibrated displays, but on a
regular screen (like the one on my ThinkPad from a couple years ago) it can be
really difficult to tell some colors apart. Selenized makes the differences
clearer.

<!-- TODO: add picture with git log -->



Slightly higher contrast
------------------------

Ethan says on Solarized website that he had tested it in a variety of lighting
conditions.  However, in practice I have encountered numerous situations when
Solarized readability was not satisfactory. This is confirmed by [Web Content
Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/),
which requires contrast of [4.5 for AA
grade](https://www.w3.org/TR/WCAG21/#contrast-minimum) and [7.0 for AAA
grade](https://www.w3.org/TR/WCAG21/#contrast-enhanced):

| color/color combination      | Solarized                    | Selenized dark               | Selenized black                                 |
| ---------------------------- | ---------                    | --------------               | ---------------                                 |
| main content (foreground)    | 4.75 - AA :heavy_check_mark: | 6.07 - AA :heavy_check_mark: | 9.05 - AAA :heavy_check_mark::heavy_check_mark: |
| fg on bg highlight           | 4.11 - :thinking:\*          | 5.04 - AA :heavy_check_mark: | 7.81 - AAA :heavy_check_mark::heavy_check_mark: |
| secondary content (comments) | 2.79 - AA :x:                | 3.23 - :thinking:\*          | 3.97 - :thinking:\*                             |
| red (darkest accent color)   | 3.25 - :thinking:\*          | 3.71 - :thinking:\*          | 4.79 - AA :heavy_check_mark:                    |

:thinking:\* _WCAG says that contrast of 3.0 is acceptable if the font has
sufficient size and weight. 3.0 is also the minimum contrast for body text
required by ISO-9241-3._

<!-- sele vs sola screenshot -->

Contrast in Selenized remains moderately low, but it is significantly more
readable in poor lighting than Solarized.



Better lightness
----------------

Solarized dark may work well when used all by itself, but it's *too dark* when
placed next to a window with high-contrast content:

![Solarized next to black&white Wikipedia](http://i.imgur.com/UlOxerG.png)

This is even more visible when Solarized dark is used for code snippets on
a website with white background:

![short code sample with Solarized](http://i.imgur.com/vStjfca.png)

Selenized dark, being slightly lighter and having more contrast,
doesn't have this problem:

![Selenized next to black&white Wikipedia](http://i.imgur.com/OX2Ce2r.png)

![short code sample with Selenized](http://i.imgur.com/fm8Orae.png)



Better terminal compatibility
-----------------------------

Solarized puts both light and dark variants in one color palette, resulting in
a weird mapping of ANSI color codes to actual colors. For example,
Solarized maps color code meant for bright/bold green to "base 01" (greyish
shade used for comments):

![color code assignment - solarized](http://i.imgur.com/Rn3yhw1.png)

Because of that many command line programs will produce strange or unreadable
output (see examples
[here](https://github.com/altercation/solarized/issues/220) and
[here](http://stackoverflow.com/questions/14093554/vim-solarized-on-os-x-terminal-app-incorrect-colors)).

Selenized keeps standard meaning of terminal color codes:

![color code assignment - selenized](http://i.imgur.com/h6Rog02.png)

