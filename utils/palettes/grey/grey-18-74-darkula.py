import selenized_base

# Variant based on fg and bg lightness of darkula palette from Jetbrains
name = "Darkula"

palette = selenized_base.generate_palette(
    background=(18, 0, 0),
    # actual foreground shade is  74, -3, -9
    foreground=(74, 0, 0),
)

