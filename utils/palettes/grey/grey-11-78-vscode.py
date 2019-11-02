import selenized_base

# Variant based on fg and bg of default VS Code palette
name = "VS Code"

palette = selenized_base.generate_palette(
    background=(11, 0, 0),
    foreground=(78, 0, 0),
)

