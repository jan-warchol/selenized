highlight clear
let g:colors_name = "selenized"

if exists("syntax_on")
    syntax reset
endif

hi Normal       cterm=NONE    ctermfg=NONE ctermbg=NONE

" interface elements
hi IncSearch    ctermfg=1    ctermbg=NONE cterm=reverse
hi Search       ctermfg=NONE ctermbg=NONE cterm=reverse
hi LineNr       ctermfg=7    ctermbg=0
hi CursorLineNr ctermfg=NONE ctermbg=NONE
hi Visual       ctermfg=NONE ctermbg=8    cterm=NONE
hi CursorLine   ctermfg=NONE ctermbg=0    cterm=NONE
hi CursorColumn ctermfg=NONE ctermbg=0    cterm=NONE
hi ColorColumn  ctermfg=NONE ctermbg=0    cterm=NONE
hi MatchParen   ctermfg=3    ctermbg=8    cterm=bold
hi Folded       ctermfg=NONE ctermbg=0    cterm=NONE
hi Pmenu        ctermfg=7    ctermbg=0
hi PmenuSel     ctermfg=NONE ctermbg=8

" diffing
hi DiffAdd      ctermfg=2    ctermbg=0    cterm=NONE
hi DiffChange   ctermfg=NONE ctermbg=0    cterm=NONE
hi DiffDelete   ctermfg=1    ctermbg=0    cterm=NONE
hi DiffText     ctermfg=0    ctermbg=3    cterm=NONE

" syntax highlig

" Comments, duh
hi Comment    ctermfg=7

" Actually this is for keywords, not whole statements
hi Statement  ctermfg=3      cterm=bold
" " `const` in javascript
" hi Keyword    ctermfg=6
" " `in` in Python 
" hi Operator   ctermfg=7      cterm=bold

" any kind of literal
hi Constant   ctermfg=9
" Strings - they are treated as a subcategory of constants
hi String     ctermfg=2

" Special characters like \n
hi Special    ctermfg=4
" hi Delimiter  ctermfg=NONE

hi PreProc    ctermfg=12 cterm=bold
" hi Define     ctermfg=4
" hi Macro      ctermfg=4

hi Identifier ctermfg=5
" hi Function   ctermfg=15

hi Type       ctermfg=2

hi Ignore     ctermfg=NONE cterm=bold

hi Underlined ctermfg=12

" Any kind of wrong syntax
hi Error      ctermfg=1      ctermbg=0     cterm=reverse

hi Todo       ctermfg=Yellow ctermbg=black cterm=reverse

