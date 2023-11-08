#!/usr/bin/env python
# import sys
# sys.settrace()
from PIL import Image
import imagequant


def main():
    input_image = Image.open("./example.png")
    output_image = imagequant.quantize_pil_image(
        input_image,
        dithering_level=1.0,
        max_colors=256,
        min_quality=20,
        max_quality=100,
    )
    output_image.save("./out.png", format="PNG")


if __name__ == "__main__":
    main()
