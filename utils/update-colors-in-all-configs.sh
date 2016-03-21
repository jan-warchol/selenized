if [ -z "$1" ]; then
    echo "no replacement pattern given"
    exit
fi
mapping_file=$(readlink --canonicalize "$1")

IFS=$(echo -en "\n")
FILES_TO_UPDATE=(
    "README.md"
    "gnome-terminal/colors/black/bd_color"
    "gnome-terminal/colors/black/bg_color"
    "gnome-terminal/colors/black/fg_color"
    "gnome-terminal/colors/black/palette"
    "gnome-terminal/colors/dark/bd_color"
    "gnome-terminal/colors/dark/bg_color"
    "gnome-terminal/colors/dark/fg_color"
    "gnome-terminal/colors/dark/palette"
    "gnome-terminal/colors/medium/bd_color"
    "gnome-terminal/colors/medium/bg_color"
    "gnome-terminal/colors/medium/fg_color"
    "gnome-terminal/colors/medium/palette"
    "iterm/Selenized black.itermcolors"
    "iterm/Selenized dark.itermcolors"
    "iterm/Selenized medium.itermcolors"
    "konsole/Selenized-black.colorscheme"
    "konsole/Selenized-dark.colorscheme"
    "konsole/Selenized-medium.colorscheme"
    "terminator/config"
    "urxvt/selenized-black.xdefaults"
    "urxvt/selenized-dark.xdefaults"
    "urxvt/selenized-medium.xdefaults"
)

# go to selenized root dir
cd ../

for file in ${FILES_TO_UPDATE[*]}; do
    echo "processing $file"
    ./utils/colorchanger.py "$mapping_file" "$file" > /dev/null
done
