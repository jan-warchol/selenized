Selenized for Emacs
===================

Dark and light Emacs 26+ themes using the Selenized palettes. Syntax colors
match the Vim theme: yellow keywords, cyan constants and strings, green types,
bright-blue functions and identifiers.

Installation
------------

1. Add this directory to `custom-theme-load-path` in your init file:

       (add-to-list 'custom-theme-load-path
                    "/path/to/selenized/editors/emacs")

2. Load a variant:

       (load-theme 'selenized-dark t)

   or

       (load-theme 'selenized-light t)

`M-x selenized-toggle-theme` switches between dark and light.

Black and white variants are not included yet.

Syntax coloring
---------------

Selenized does not copy every Solarized token choice. Keywords are yellow, not
green; see [issue 74](https://github.com/jan-warchol/selenized/issues/74).
Colors come from [the-values.md](../../the-values.md) and stay inside the
official 22-color palettes.
