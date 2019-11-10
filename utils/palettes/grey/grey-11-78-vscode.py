import selenized_base

name = "Variant based on fg and bg of default VS Code palette"

palette = selenized_base.generate_palette(
    background=(11, 0, 0),
    foreground=(78, 0, 0),
)

