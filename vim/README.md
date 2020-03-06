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


Contributing
------------

Selenized theme files are generated using
[vim-colortemplate](https://github.com/lifepillar/vim-colortemplate). You need
to install the plugin (note that it requires Vim 8), edit `.colortemplate`
files and run `:Colortemplate!` to regenerate theme files.

It's quite straighforward to use, and in case anything is not clear the
documentation is really helpful.
