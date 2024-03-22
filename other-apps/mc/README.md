# Selenized skin for Midnight Commander

## Installation

Download skin file to your MC config directory to be able to use it.

1. Download to current user directory:
   
       $ mkdir -p $HOME/.local/share/mc/skins/
       $ wget https://raw.githubusercontent.com/jan-warchol/selenized/master/other-apps/mc/selenized.ini -P $HOME/.local/share/mc/skins/

2. Or setup it system-wide:
   
       # wget https://raw.githubusercontent.com/jan-warchol/selenized/master/other-apps/mc/selenized.ini -P /usr/share/mc/skins/

## Usage

After that you need to choose skin in MC. There are several ways to do so:

1. Configure via UI: in menu `Options -> Appearances` set `Skin` field to `selenized`.
2. Run MC with selected theme:
   
       $ mc -S selenized
   
4. Configure selected skin via environment variable:

       $ echo "export MC_SKIN=$HOME/.local/share/mc/skins/selenized.ini" >> $HOME/.bashrc
   
    Keep in mind that you need to restart your terminal or reload your `.bashrc` manually for these changes to have effect.
