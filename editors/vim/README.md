🔥 **I need your opinion!** 🔥

There are some design decisions that need to be made to complete Vim support.
Your feedback would be very helpful - please comment on
[issue 68](https://github.com/jan-warchol/selenized/issues/68) and
[issue 74](https://github.com/jan-warchol/selenized/issues/74).


Installation
------------

1. Copy theme file(s) inside your `$HOME/.vim/colors/` directory
   (`colors/selenized.vim` for dark&light themes, `colors/selenized_bw.vim` for
   black&white themes).
1. Inside vim, use `:colorscheme selenized` to switch colorscheme to selenized.
   You can also make this setting permanent by adding line `colorscheme
   selenized` to your `.vimrc`.
1. Use `set background=dark` and `set background=light` to switch between versions

There are some additional steps if you use vim inside terminal.

### Truecolor-enabled terminals

If your terminal [supports true
color](https://gist.github.com/XVilka/8346728#now-supporting-true-color), add
`set termguicolors` to your `.vimrc`.

### Other terminals

1. Configure your terminal emulator (e.g. [gnome-terminal](../gnome-terminal),
   [iTerm](../iterm) etc.) to use selenized palette
1. You may have to add `set t_Co=16` to your `.vimrc` to instruct Vim to use
   ANSI colors rather then trying 256-color variant of the palette (which is
   only an approximation, see [this
   issue](https://github.com/jan-warchol/selenized/issues/65) for more details)


Syntax coloring choices
-----------------------

Selenized aims to have a similar feel to Solarized, but it doesn't follow all
Solarized coloring choices. In particular, I believe that using **green for
keywords** doesn't look good, so I've made them yellow (swapping with types,
which are yellow in Solarized). If you don't like this choice, add this to your
`.vimrc`:

    let g:selenized_green_keywords=1

Also note that selenized uses **orange and violet** only in the GUI/truecolor
version of the theme.  That's because they are not available in ANSI color
palette (Solarized worked around this with an [ugly
hack](https://github.com/jan-warchol/selenized/blob/master/whats-wrong-with-solarized.md#problems-with-implementation),
but I prefer to keep compatibility).


Contributing
------------

Selenized theme files are generated using
[vim-colortemplate](https://github.com/lifepillar/vim-colortemplate). You need
to install the plugin (note that it requires Vim 8), edit `.colortemplate`
files and run `:Colortemplate!` to regenerate theme files.

It's quite straighforward to use, and in case anything is not clear the
documentation is really helpful.
