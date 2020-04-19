#!/bin/bash

# This scripts prints a full set of color codes, normal and bright/bold,
# used on both foreground and background.

TEXT_BLOCK="■■■■"
SPACE_BLOCK="    "
reset_colors() { echo -en "\033[0m${1}\033[0m"; }
# for testing solarized which uses strange color mapping...
COMMENT_COLOR=${1:-37}

allcolors() {
    # $1 - modifier (format), $2 - row header, $3 - row comment
    reset_colors "$(printf '%10s' $1)__ "
    for color_code in 30 31 32 33 34 35 36 37; do
        echo -en "\033[${1}${color_code}m${2} "; reset_colors
    done
    reset_colors " \033[${COMMENT_COLOR}m${3} \n"
}

reset_colors "\n"
echo -en "\033[${COMMENT_COLOR}m" 
echo -e "      Color: black red green yel blue pink cyan white\033[0m"
echo -e "       ANSI:  30   31   32   33   34   35   36   37"

allcolors ""      "text"         "normal"
allcolors "1;"    "text"         "bold"
allcolors "7;"    "$SPACE_BLOCK" "reverse"
allcolors "1;7;"  "$SPACE_BLOCK" "bold reverse"

echo "        \\"
echo "         Additional formatting"

reset_colors "\n "
echo -e " Default foreground: text \033[7m$SPACE_BLOCK \033[0m"\
        " Bold foreground: \033[1mtext \033[7m$SPACE_BLOCK \n"

