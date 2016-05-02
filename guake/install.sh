#!/usr/bin/env bash

dir=`dirname $0`

# palette variant
VARIANT=${1:-medium}

gconftool-2 -s -t string /apps/guake/style/background/color `cat $dir/colors/$VARIANT/bg_color`
gconftool-2 -s -t string /apps/guake/style/font/color `cat $dir/colors/$VARIANT/fg_color`
gconftool-2 -s -t string /apps/guake/style/font/palette `cat $dir/colors/$VARIANT/palette`

