highlight clear
let g:colors_name = "Selenized"

if exists("syntax_on")
    syntax reset
endif

" GUI color definitions for selenized medium
let s:guibg1     = "#154053"
let s:guibg2     = "#1b5269"
let s:guibg3     = "#366981"
let s:guifg1     = "#77919c"
let s:guifg2     = "#a8bcc3"
let s:guifg3     = "#c4d8df"

let s:guired     = "#fc5851"
let s:guigreen   = "#78b93e"
let s:guiyellow  = "#d8b033"
let s:guiblue    = "#4e97f5"
let s:guimagenta = "#f16dc5"
let s:guicyan    = "#41c7b9"

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
exe "hi ColorColumn  cterm=NONE                 ctermbg=0                                   guibg=".s:guibg2
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
exe "hi Todo         cterm=reverse ctermfg=3    ctermbg=0                guifg=".s:guibg1." guibg=".s:guiyellow

