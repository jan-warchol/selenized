Selenized settings for dircolors (`ls` etc.)
============================================

`ls` command can color listed files according to their type; these coloring
rules are loaded from `dircolors` database.  Most of this coloring works well
with Selenized palette, but there is one exception: directories with
permissions set to 777 are by default displayed in blue text on green
background, which is not very readable (as green and blue have almost the same
lightness in Selenized).

I recommend overriding the coloring of 777 directories to reversed bold blue.
You can do this by appending to `LS_COLORS` env variable, like this:

    # fix dircolors for Selenized
    export LS_COLORS="$LS_COLORS:ow=1;7;34:st=30;44:su=30;41"

To make this change permanent, simply add this line to your `.bashrc` (or
similar file).

In the future I may create a fully customized dircolors configuration, tailored
specifically to selenized.
