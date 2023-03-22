#!/usr/bin/env bash
# gnomeVersion="$(expr "$(gnome-terminal --version)" : '.* \(.*[.].*[.].*\)$')"
gnomeVersion="$(gnome-terminal --version | awk '{print $4}')"
# example output on Fedora 35
# GNOME Terminal 3.42.2 using VTE 0.66.2 +BIDI +GNUTLS +ICU +SYSTEMD
echo "gnome-terminal-version=${gnomeVersion}"

# newGnome=1 if the gnome-terminal version >= 3.8
if [[ ("$(echo "$gnomeVersion" | cut -d"." -f1)" = "3" && \
       "$(echo "$gnomeVersion" | cut -d"." -f2)" -ge 8) || \
       "$(echo "$gnomeVersion" | cut -d"." -f1)" -ge 4 ]]
  then newGnome="1"
  dconfdir=/org/gnome/terminal/legacy/profiles:
else
  newGnome=0
  gconfdir=/apps/gnome-terminal/profiles
fi

die() {
  echo $1
  exit ${2:-1}
}

in_array() {
  local e
  for e in "${@:2}"; do [[ $e == $1 ]] && return 0; done
  return 1
}

to_gconf() {
    tr ' ' ':' | sed 's|:$|\n|'
}

to_dconf() {
    tr ' ' '~' | sed -e "s|\$|']\n|" -e "s|~|', '|g" -e "s|^|['|"
}
