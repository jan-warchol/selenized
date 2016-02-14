#!/bin/bash

BRIGHT="\e[97m"
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
 ${BRIGHT}Selenized${RESET} is a color palette based on Ethan Shoonover's ${BRIGHT}Solarized.${RESET}
 I have adjusted hues and lightness to decrease ambiguity and ensure
 readability in all conditions.
"
loremipsum="\n \e[0mLorem ipsum dolor sit amet, consectetur adipiscing elit."

echo -e "$loremipsum"
for color in 30 90 37 36 34 35 31 33 32 37 90 30; do
    echo -en "\e[${color}m Text"
done
echo -en "$loremipsum"
echo -en "\n
${DIM} Note how using just slightly darker color can make this note appear
 less important than the rest of the text while still being legible.${RESET}
"

echo -e "
 \e[31mRed\e[0m cannot be too bright, because it would get ${BRIGHT}desaturated.${RESET}
 \e[33mYellow\e[0m is tricky, because we are used to it being bright.
 \e[32mGreen\e[0m, on the contrary, is quite simple.
 \e[36mCyan\e[0m also has to be dimmer than what we are used to.
 \e[34mBlue\e[0m must be darker than cyan to make them clearly ${BRIGHT}different.${RESET}
 \e[35mMagenta\e[0m is quite simple again.
"
