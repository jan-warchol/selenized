# This script is for dev purposes (I test palettes in Konsole)

NAME=`basename "${1%%.konsole}"`

# copy palette
cp "$1" "$HOME/.kde/share/apps/konsole/$NAME.colorscheme"

# create a profile
cat <<EOF > "$HOME/.kde/share/apps/konsole/$NAME.profile"
[Appearance]
AntiAliasFonts=true
BoldIntense=true
ColorScheme=$NAME
Font=Ubuntu Mono,12,-1,5,50,0,0,0,0,0

[General]
Name=$NAME
Parent=FALLBACK/

[Scrolling]
ScrollBarPosition=2
EOF

# add profile to menu
grep --quiet "Favorites=.*${NAME}" "$HOME/.kde/share/config/konsolerc" || \
sed -i "s/Favorites=/Favorites=${NAME}.profile,/" \
       "$HOME/.kde/share/config/konsolerc"

