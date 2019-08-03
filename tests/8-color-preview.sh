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
    sequence=(31 "31;1" 33 32 36 34 "34;1" 35)

    reset_colors "$(printf '%6s') "
    echo -en "\033[${COMMENT_COLOR}m"
    for ansi_code in ${sequence[*]}; do
        printf '%5s' "${ansi_code}"
    done

    echo ""
    reset_colors "$(printf '%6s' $1)_ "
    for ansi_code in ${sequence[*]}; do
        echo -en "\033[${1}${ansi_code}m${2} "; reset_colors
    done
    reset_colors " \033[${COMMENT_COLOR}m${3} \n"
}

reset_colors "\n"

allcolors ""       "text"         "text"
echo
allcolors "7;"   "$SPACE_BLOCK" "reverse"

reset_colors "\n"
echo -e "\033[0m Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n"

