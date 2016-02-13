#!/bin/bash

echo "
                        _            _             _
               ___  ___| | ___ _ __ (_)_______  __| |
              / __|/ _ \ |/ _ \ '_ \| |_  / _ \/ _' |
              \__ \  __/ |  __/ | \ | |/ /  __/ (_| |
              |___/\___|_|\___|_| |_|_/___\___|\__,_|

                 Readability and comfort above all

                        author: Jan Warchoł
                               v0.2
"

echo -en "\e[0m            "
for color in 0 7 6 4 5 1 3 2 7 0; do
    echo -en "\e[4${color}m    "
done
echo -e "\e[0m"

echo -n "
 Selenized is a color palette based on Solarized (by Ethan Shoonover).
 I have adjusted hues and lightness to decrease ambiguity and ensure
 readability in all conditions.
"
loremipsum="\n \e[0mLorem ipsum dolor sit amet, consectetur adipiscing elit."

echo -e "$loremipsum"
for color in 30 37 36 34 35 31 33 32 37 30; do
    echo -en "\e[${color}m Text "
done
echo -e "$loremipsum"

echo -e "
 \e[31mRed\e[0m cannot be too bright, because it would get desaturated.
 \e[33mYellow\e[0m is tricky, because we are used to it being bright.
 \e[32mGreen\e[0m, on the contrary, is quite simple.
 \e[36mCyan\e[0m also has to be dimmer than what we are used to.
 \e[34mBlue\e[0m must be darker than cyan to make them clearly different.
 \e[35mMagenta\e[0m is quite simple again.
"
