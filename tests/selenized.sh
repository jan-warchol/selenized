#!/bin/bash

BRIGHT="\e[97m"
BOLD="\e[1;37m"
DIM="\e[90m"
RESET="\e[0m"

echo -e "$BRIGHT
                         _            _             _
                ___  ___| | ___ _ __ (_)_______  __| |
               / __|/ _ \ |/ _ \ '_ \| |_  / _ \/ _' |
               \__ \  __/ |  __/ | \ | |/ /  __/ (_| |
               |___/\___|_|\___|_| |_|_/___\___|\__,_|
$RESET
                  Readability and comfort above all

                  $DIM       author: Jan Warchoł
                                v0.3        $RESET
"

echo -en "\e[0m          "
for color in 40 100 47 46 44 45 41 43 42 47 100 40; do
    echo -en "\e[${color}m    "
done
echo -e "\e[0m"

echo -ne "
 ${BOLD}Selenized${RESET} is a color palette based on Ethan Shoonover's ${BOLD}Solarized.${RESET}
 I have adjusted hues and lightness to decrease ambiguity and ensure
 readability in all conditions.
"

echo -en "
${DIM} Note how using just slightly darker color can make this note appear
 less important than the rest of the text while still being legible.${RESET}
"

loremipsum="\n \e[0mLorem ipsum dolor sit amet, consectetur adipiscing elit."
echo -en "$loremipsum\n   "
for color in 90 37 36 34 35 31 33 32 37 90; do
    echo -en "\e[${color}m Text"
done
echo -e "$loremipsum\n"
