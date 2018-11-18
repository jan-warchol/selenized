Selenized skin for Midnight Commander
=====================================

*Note: this is just a very rough initial version.  I don't use Midnight
Commander myself, so any improvements will be welcome!*

Installation
------------

Download skin file and set `MC_SKIN` env variable to point to it:

    mkdir -p $HOME/.mc/; cd $HOME/.mc/
    wget https://raw.githubusercontent.com/jan-warchol/selenized/master/mc/selenized.ini
    echo "export MC_SKIN=$HOME/.mc/selenized.ini" >> $HOME/.bashrc

Keep in mind that you need to restart your terminal or reload your `.bashrc`
manually for these changes to have effect.
