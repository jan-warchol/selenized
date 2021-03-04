🔥Disclaimer!🔥
--------------

(Author of Selenized Dark theme: https://github.com/judu)

This is a modified Solarized Dark (Darcula) from IntelliJ.
There only is a Selenized Dark theme for now. If you need the light one, you are free to
take the light one and replace occurrences of bg and fg colors.

I'm not doing it myself because I know I will not test the light theme enough.

## What I did to make the theme

- search and replace all occurrences of solarized colors by matching selenized ones;
- fixed the console bright colors with actual `br_xxx` colors from selenized;
- take all remaining colors and check them:
  - some colors were "solarized colors with a tiny difference" (like #073643 or #083641 which are almost #073642):
    I translated them all to the selenized color matching the closest solarized color (in
    the example, `bg_1` #184956);
  - some colors were "solarized colors with a not so tiny difference" (like #083f4d which
    is basically #073642 but +01+09+09 🤷): I took the matching selenized color and
    applied the same transformation: #19525f


## Languages color choices

Since I just changed solarized colors to selenized ones, I have not thought about [issue 68](https://github.com/jan-warchol/selenized/issues/68) and
[issue 74](https://github.com/jan-warchol/selenized/issues/74). Feel free to amend my work
with whatever comes out of this discussion.



