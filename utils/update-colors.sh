# I use this script for updating all occurrences of a color value in selenized
# repository (as well as my private terminator config repository) after
# changing the value.

declare -A dict_of_changes=(
  [v0.2]=v0.3
)

update_colors() {
    for from_string in "${!dict_of_changes[@]}"; do
        to_string=${dict_of_changes[$from_string]}
        git sed "s/$from_string/$to_string/gi"
    done
}

# switch to directory containing this script
cd $(dirname $(readlink --canonicalize "$0"))
update_colors

# also update colors in my private terminator config repo
cd ~/.config/terminator
update_colors

