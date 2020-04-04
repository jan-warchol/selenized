Using selenized palette
-----------------------

Guidelines for creating a selenized theme for your terminal emulator.

Each Selenized variant defines 3 background shades (`bg_*`), 3 content shades
(`dim_*`, `fg_*`) and 8 accent colors (each with a bright version). This
document explains which color to use for what. You can find [RGB values of the
colors **here**](the-values.md).


### Color mapping

| Element           | Color  |
| ----------------- | ------ |
| background        | bg_0   |
| foreground        | fg_0   |
| bold foreground   | fg_1   |
| dim foreground    | dim_0  |
| cursor color      | fg_1   |
| selection         | bg_2   |
| selection text    | (none) |

Notes:

* Most terminals don't allow setting selection colors, they simply reverse
  foreground and background.
* Some terminals allow setting the opacity/brightness of special "dim" colors.
  This value should be set to 0.625.
* In case your terminal has a setting like "bright background", set it to
  `bg_1`.
* ANSI colors don't include orange and violet, so they are not used in terminal
  emulators - they are intended for GUI applications.



ANSI palette:

| #   | ANSI color     | Selenized color |
| --- | -------------- | --------------- |
| 0   | black          | bg_1            |
| 1   | red            | red             |
| 2   | green          | green           |
| 3   | yellow         | yellow          |
| 4   | blue           | blue            |
| 5   | magenta        | magenta         |
| 6   | cyan           | cyan            |
| 7   | white          | dim_0           |
|     |                |                 |
| 8   | bright black   | bg_2            |
| 9   | bright red     | br_red          |
| 10  | bright green   | br_green        |
| 11  | bright yellow  | br_yellow       |
| 12  | bright blue    | br_blue         |
| 13  | bright magenta | br_magenta      |
| 14  | bright cyan    | br_cyan         |
| 15  | bright white   | fg_1            |


### Creating a template

Theme files should be generated from templates (so that it's easy to create
configs for all selenized variants, and update them whenever colors change).

See
[`utils/templates/template-test.example.template`](./utils/templates/template-test.example.template)
for an example template and [`utils/README.md`](./utils/README.md) for
instructions on how to use templating machinery.

That's it!

Please send me a [pull request](https://github.com/jan-warchol/selenized/pulls)
with the resulting configs and template so that I can make your terminal
officially supported :-)

