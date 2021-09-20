#!/usr/bin/env python

from PIL import Image
import imagequant


def main():
    input_image = Image.open("./example.png")
    output_image = imagequant.quantize_pil_image(input_image)
    output_image.save("./out.png", format="PNG")


if __name__ == "__main__":
    main()
