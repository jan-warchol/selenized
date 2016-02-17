#!/bin/bash

echo -en "\n\e[0m    "
for color in 40 47 46 44 45 41 43 42 47 40; do
    echo -en "\e[${color}m    "
done
echo -e "\e[0m"

echo -en "\e[0m    "
for color in 100 107 106 104 105 101 103 102 107 100; do
    echo -en "\e[1;${color}m    "
done
echo -e "\e[0m\n"

