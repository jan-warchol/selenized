highlight clear
let g:colors_name = "Selenized"

if exists("syntax_on")
    syntax reset
endif

hi Normal       cterm=NONE ctermfg=NONE ctermbg=NONE        guibg=#1b1b1b guifg=#ababab

" interface elements
hi IncSearch    cterm=reverse                               gui=reverse
hi Search       cterm=reverse ctermfg=NONE ctermbg=NONE     gui=reverse guifg=NONE guibg=NONE
hi LineNr       ctermfg=7 ctermbg=0                         guifg=#777777 guibg=#2d2d2d
hi CursorLineNr ctermfg=NONE ctermbg=NONE                   guifg=NONE guibg=NONE
hi Visual       cterm=NONE ctermfg=NONE ctermbg=8           guibg=#474747
hi Cursor                                                   guifg=bg guibg=fg
hi CursorLine   cterm=NONE    ctermbg=0                     guibg=#2d2d2d
hi CursorColumn cterm=NONE    ctermbg=0                     guibg=#2d2d2d
hi MatchParen   cterm=reverse ctermbg=NONE ctermfg=darkcyan

" Diffing
hi DiffAdd      cterm=none ctermfg=green   ctermbg=black
hi DiffChange   cterm=none ctermfg=none    ctermbg=black
hi DiffDelete   cterm=none ctermfg=darkred ctermbg=black
hi DiffText     cterm=none ctermfg=black   ctermbg=darkyellow

" syntax highlig
hi String       ctermfg=darkblue                            guifg=#3182de
hi Comment      ctermfg=gray                                guifg=#777777
hi Constant     ctermfg=1                                   guifg=#e3413f
hi Special      ctermfg=5                                   guifg=#dd5ab2
hi Identifier   ctermfg=6                                   guifg=#2cb8aa
hi Statement    ctermfg=3                                   guifg=#c9a223
hi PreProc      ctermfg=5                                   guifg=#dd5ab2
hi Type         ctermfg=2                                   guifg=#67a82d
hi Ignore       cterm=bold ctermfg=7                        gui=bold guifg=#ababab
hi Error        cterm=bold ctermfg=7 ctermbg=1              gui=bold guifg=#777777 guibg=#e3413f
hi Todo         ctermfg=0 ctermbg=3                         guifg=#1b1b1b guibg=#c9a223

