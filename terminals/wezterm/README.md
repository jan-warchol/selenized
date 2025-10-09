Selenized color palette for WezTerm
=================================

Installation
------------

- Copy `selenized-*.toml` to WezTerm's custom scheme directory. See [WezTerm: Defining a Color Scheme in a separate file](https://wezfurlong.org/wezterm/config/appearance.html#defining-a-color-scheme-in-a-separate-file)

- Config `wezterm.lua` to use the color scheme:

  ```lua
  config.color_scheme = 'selenized-dark'
  ```

  You may also automatically adjust the color scheme based on system dark/light mode. See [`wezterm.gui.get_appearance()`](https://wezfurlong.org/wezterm/config/lua/wezterm.gui/get_appearance.html).