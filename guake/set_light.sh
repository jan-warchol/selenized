#!/usr/bin/env bash

dir=`dirname $0`

PROFILE=${1:-Default}

#######
# for guake
gconftool-2 -s -t string /apps/guake/style/background/color `cat $dir/colors/base3`
gconftool-2 -s -t string /apps/guake/style/font/color `cat $dir/colors/base00`
gconftool-2 -s -t string /apps/guake/style/font/palette `cat $dir/colors/palette`
