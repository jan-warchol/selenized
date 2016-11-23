highlight clear
let g:colors_name = "Selenized"

if exists("syntax_on")
    syntax reset
endif

highlight DiffAdd cterm=none ctermfg=green ctermbg=black
highlight DiffDelete cterm=none ctermfg=darkred ctermbg=black
highlight DiffChange cterm=none ctermfg=none ctermbg=black
highlight DiffText cterm=none ctermfg=black ctermbg=darkyellow

highlight LineNr ctermfg=lightgray ctermbg=black
highlight String ctermfg=darkblue
highlight Comment ctermfg=gray
highlight CursorLine ctermbg=black cterm=NONE
highlight CursorColumn ctermbg=black cterm=NONE

highlight Search cterm=reverse ctermfg=NONE ctermbg=NONE
highlight Visual cterm=NONE ctermfg=NONE  ctermbg=darkgray
highlight MatchParen cterm=reverse ctermbg=NONE ctermfg=darkcyan

