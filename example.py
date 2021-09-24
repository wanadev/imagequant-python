#!/usr/bin/env python

from PIL import Image
import imagequant


def main():
    input_image = Image.open("./example.png")
    output_image = imagequant.quantize_pil_image(
        input_image,
        dithering_level=1.0,
        max_colors=256,
    )
    output_image.save("./out.png", format="PNG")


if __name__ == "__main__":
    main()
