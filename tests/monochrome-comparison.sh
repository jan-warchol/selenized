# Define vars with color codes - may be handy for other things, too
ZERO="\e[0m"
BOLD="\e[1m"
ITAL="\e[3m"
UNDR="\e[4m"

COL1="\e[91m"
COL2="\e[92m"
COL3="\e[93m"
COL4="\e[94m"
COL5="\e[95m"
COL6="\e[96m"
COL7="\e[97m"

print_all_styles() {
  color1=${1}
  color2=${2:-$1}

  echo -e -n        ${UNDR}${color2}foobar${ZERO} "  "
  echo -e -n        ${ZERO}${color2}foobar${ZERO} "  "
  echo -e -n        ${ITAL}${color2}foobar${ZERO} "  "
  echo ""
  echo -e -n ${UNDR}${BOLD}${color1}foobar${ZERO} "  "
  echo -e -n        ${BOLD}${color1}foobar${ZERO} "  "
  echo -e -n ${ITAL}${BOLD}${color1}foobar${ZERO} "  "
  echo ""
}

print_all_styles $COL2
print_all_styles $COL3
print_all_styles $COL4
print_all_styles $COL5
print_all_styles $COL7
