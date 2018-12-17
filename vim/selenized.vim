highlight clear
let g:colors_name = "Selenized"

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

" diffing
hi DiffAdd      ctermfg=2    ctermbg=0    cterm=NONE
hi DiffChange   ctermfg=NONE ctermbg=0    cterm=NONE
hi DiffDelete   ctermfg=1    ctermbg=0    cterm=NONE
hi DiffText     ctermfg=0    ctermbg=3    cterm=NONE

" syntax highlig

" Comments, duh
hi Comment    ctermfg=7
" Actually this is for keywords, not whole statements
hi Statement  ctermfg=7      cterm=bold
" `const` in javascript
hi Keyword    ctermfg=1      cterm=underline
" `in` in Python 
hi Operator   ctermfg=7      cterm=bold
" Strings, duh
hi String     ctermfg=2
" any kind of contstants, including strings
hi Constant   ctermfg=3
hi JavaScriptNumber   ctermfg=3
" Special characters like \n
hi Special    ctermfg=6

hi Character  ctermfg=NONE
hi Identifier ctermfg=NONE
hi Function   ctermfg=NONE
hi Delimiter  ctermfg=NONE
hi PreProc    ctermfg=NONE
hi Type       ctermfg=NONE
hi Ignore     ctermfg=NONE   cterm=bold

" Any kind of wrong syntax
hi Error      ctermfg=1      ctermbg=0     cterm=reverse

" hi Todo       ctermfg=Yellow ctermbg=black cterm=reverse

" " syntax highlig
" hi String                     ctermfg=4
" hi Comment                    ctermfg=7
" hi Constant                   ctermfg=1
" hi Special                    ctermfg=5
" hi Identifier                 ctermfg=6
" hi Statement                  ctermfg=3
" hi PreProc                    ctermfg=5
" hi Type                       ctermfg=2
" hi Ignore       cterm=bold    ctermfg=7
" hi Error        cterm=bold    ctermfg=7    ctermbg=1
" hi Todo         cterm=reverse ctermfg=3    ctermbg=0

