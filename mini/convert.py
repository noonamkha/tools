import cairosvg

def svg_to_png(input_svg_path, output_png_path, width=None, height=None, scale=1.0):
    """
    Convert an SVG file to a PNG file with transparent background.

    :param input_svg_path: Path to input SVG file
    :param output_png_path: Path to output PNG file
    :param width: Optional output width in pixels
    :param height: Optional output height in pixels
    :param scale: Optional scale factor (default 1.0)
    """
    cairosvg.svg2png(
        url=input_svg_path,
        write_to=output_png_path
    )

# Example usage
svg_to_png("nk_sign.svg", "output.png", scale=2.0)