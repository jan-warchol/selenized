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
    reset_colors "$(printf '%6s' $1)_ "
    for color_code in 1 "1;1" 2 3 4 "4;1" 5 6; do
        echo -en "\033[${1}${color_code}m${2} "; reset_colors
    done
    reset_colors " \033[${COMMENT_COLOR}m${3} \n"
}

reset_colors "\n"
echo -en "\033[${COMMENT_COLOR}m" 
echo -e "        red  orng grn  yel  blue viol pink cyan  \033[0m"

allcolors 3       "text"         "text"
echo ""
allcolors "7;3"   "$SPACE_BLOCK" "reverse"

echo "   |\\"
echo "   | Color code (listed in column header)"
echo "   Formatting attribute(s)"

reset_colors "\n"
echo -e "\033[0m Lorem ipsum dolor sit amet, consectetur adipiscing elit."

