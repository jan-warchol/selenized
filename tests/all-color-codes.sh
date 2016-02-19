#!/bin/bash

# This scripts prints a full set of color codes, normal and bright, used on
# both foreground and background.

text_block="■■■■"
space_block="    "
reset() { echo -en "\033[0m$1"; }

allcolors() {
  # $1 - modifier (format), $2 - text to print
  reset "  "
  for color in 0 1 2 3 4 5 6 7 8 9; do
      echo -en "\033[${1}${color}m${2} "
      # echo -en "\033[49;3${color}m${color}""\033[${1}${color}m${2} "
  done
  reset " $1 \n"
}

reset "\n"
echo -e "  Foreground: $text_block"
echo -e "  $(tput bold)Bold foreground: $text_block"
reset "\n"

echo "    0    1    2    3    4    5    6    7    8    9"
allcolors 3 "$text_block"
allcolors 9 "$text_block"
allcolors 4 "$space_block"
allcolors 10 "$space_block"
allcolors 3 "BBBB"
allcolors "1;3" "BBBB"

reset "\n"
echo -e "\033[0mLorem ipsum dolor sit amet, consectetur adipiscing elit."

