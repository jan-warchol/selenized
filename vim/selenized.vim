highlight clear
let g:colors_name = "Selenized"

if exists("syntax_on")
    syntax reset
endif

hi Normal       cterm=NONE    ctermfg=NONE ctermbg=NONE

" interface elements
hi IncSearch    cterm=reverse ctermfg=red  ctermbg=NONE
hi Search       cterm=reverse ctermfg=NONE ctermbg=NONE
hi LineNr                     ctermfg=7    ctermbg=0
hi CursorLineNr               ctermfg=NONE ctermbg=NONE
hi Visual       cterm=NONE    ctermfg=NONE ctermbg=8
hi Cursor
hi CursorLine   cterm=NONE                 ctermbg=0
hi CursorColumn cterm=NONE                 ctermbg=0
hi ColorColumn  cterm=NONE                 ctermbg=0
hi MatchParen   cterm=reverse ctermfg=6    ctermbg=NONE
hi Folded       cterm=NONE    ctermfg=NONE ctermbg=0

" diffing
hi DiffAdd      cterm=NONE    ctermfg=2    ctermbg=0
hi DiffChange   cterm=NONE    ctermfg=NONE ctermbg=0
hi DiffDelete   cterm=NONE    ctermfg=1    ctermbg=0
hi DiffText     cterm=NONE    ctermfg=0    ctermbg=3

" syntax highlig
hi String                     ctermfg=4
hi Comment                    ctermfg=7
hi Constant                   ctermfg=1
hi Special                    ctermfg=5
hi Identifier                 ctermfg=6
hi Statement                  ctermfg=3
hi PreProc                    ctermfg=5
hi Type                       ctermfg=2
hi Ignore       cterm=bold    ctermfg=7
hi Error        cterm=bold    ctermfg=7    ctermbg=1
hi Todo         cterm=reverse ctermfg=3    ctermbg=0

