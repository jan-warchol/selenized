#!/usr/bin/env bash

dir=`dirname $0`

PROFILE=${1:-Default}

gconftool-2 -s -t string /apps/guake/style/background/color `cat $dir/colors/base03`
gconftool-2 -s -t string /apps/guake/style/font/color `cat $dir/colors/base0`
gconftool-2 -s -t string /apps/guake/style/font/palette `cat $dir/colors/palette`

