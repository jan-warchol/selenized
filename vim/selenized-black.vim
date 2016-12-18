highlight clear
let g:colors_name = "Selenized black"

if exists("syntax_on")
    syntax reset
endif

" GUI color definitions
let s:guibg1     = "#1b1b1b"
let s:guibg2     = "#2d2d2d"
let s:guibg3     = "#474747"
let s:guifg1     = "#777777"
let s:guifg2     = "#ababab"
let s:guifg3     = "#cccccc"

let s:guired     = "#e3413f"
let s:guigreen   = "#67a82d"
let s:guiyellow  = "#c9a223"
let s:guiblue    = "#3182de"
let s:guimagenta = "#dd5ab2"
let s:guicyan    = "#2cb8aa"

exe "hi Normal       cterm=NONE    ctermfg=NONE ctermbg=NONE             guifg=".s:guifg2." guibg=".s:guibg1

" interface elements
exe "hi IncSearch    cterm=reverse                           gui=reverse"
exe "hi Search       cterm=reverse ctermfg=NONE ctermbg=NONE gui=reverse guifg=NONE         guibg=NONE"
exe "hi LineNr                     ctermfg=7    ctermbg=0                guifg=".s:guifg1." guibg=".s:guibg2
exe "hi CursorLineNr               ctermfg=NONE ctermbg=NONE             guifg=NONE         guibg=NONE"
exe "hi Visual       cterm=NONE    ctermfg=NONE ctermbg=8                                   guibg=".s:guibg3
exe "hi Cursor                                                           guifg=bg           guibg=fg"
exe "hi CursorLine   cterm=NONE                 ctermbg=0                                   guibg=".s:guibg2
exe "hi CursorColumn cterm=NONE                 ctermbg=0                                   guibg=".s:guibg2
exe "hi MatchParen   cterm=reverse ctermfg=6    ctermbg=NONE"

" diffing
exe "hi DiffAdd      cterm=NONE    ctermfg=2    ctermbg=0"
exe "hi DiffChange   cterm=NONE    ctermfg=NONE ctermbg=0"
exe "hi DiffDelete   cterm=NONE    ctermfg=1    ctermbg=0"
exe "hi DiffText     cterm=NONE    ctermfg=0    ctermbg=3"

" syntax highlig
exe "hi String                     ctermfg=4                             guifg=".s:guiblue
exe "hi Comment                    ctermfg=7                             guifg=".s:guifg1
exe "hi Constant                   ctermfg=1                             guifg=".s:guired
exe "hi Special                    ctermfg=5                             guifg=".s:guimagenta
exe "hi Identifier                 ctermfg=6                             guifg=".s:guicyan
exe "hi Statement                  ctermfg=3                             guifg=".s:guiyellow
exe "hi PreProc                    ctermfg=5                             guifg=".s:guimagenta
exe "hi Type                       ctermfg=2                             guifg=".s:guigreen
exe "hi Ignore       cterm=bold    ctermfg=7                 gui=bold    guifg=".s:guifg2
exe "hi Error        cterm=bold    ctermfg=7    ctermbg=1    gui=bold    guifg=".s:guifg1." guibg=".s:guired
exe "hi Todo                       ctermfg=0    ctermbg=3                guifg=".s:guibg1." guibg=".s:guiyellow

