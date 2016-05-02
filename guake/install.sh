#!/usr/bin/env bash

dir=`dirname $0`

echo
echo -e "\e[1;39mWarning!\e[0m"
echo -e "This will permanently overwrite the default profile - there is no undo."
echo -e "Consider backing up your profile before installing Selenized."
echo
echo -n "Are you sure you want to continue? (yes/no) "

read confirmation
if [[ $(echo $confirmation | tr '[:lower:]' '[:upper:]') != YES ]]
then
  echo "ERROR: Confirmation failed -- ABORTING!"
  exit 1
fi

echo "Confirmation received -- applying settings"

# palette variant
VARIANT=${1:-medium}

gconftool-2 -s -t string /apps/guake/style/background/color `cat $dir/colors/$VARIANT/bg_color`
gconftool-2 -s -t string /apps/guake/style/font/color `cat $dir/colors/$VARIANT/fg_color`
gconftool-2 -s -t string /apps/guake/style/font/palette `cat $dir/colors/$VARIANT/palette`

