Imagequant Python - Python Bindings for libimagequant
=====================================================

**Imagequant Python** are bindings to allow using libimagequant_ from Python.

**Libimagequant** is a small, portable C library for high-quality conversion of RGBA images to 8-bit indexed-color (palette) images.

.. _libimagequant: https://github.com/ImageOptim/libimagequant


Usage
-----

With PIL / Pillow
~~~~~~~~~~~~~~~~~

.. code-block:: python

    from PIL import Image
    import imagequant

    input_image = Image.open("./example.png")
    output_image = imagequant.quantize_pil_image(
        input_image,
        dithering_level=1.0,
        max_colors=256,
    )
    output_image.save("./out.png", format="PNG")

|input_image| → |output_image|

.. |input_image| image:: ./example.png
.. |output_image| image:: ./example_out.png


With Raw Data
~~~~~~~~~~~~~

.. code-block:: python

    import imagequant

    # 2×2px image
    IMAGE_DATA = (
        # | R | G | B | A |
        b"\xFF\x00\x00\xFF"  # red
        b"\x00\xFF\x00\xFF"  # lime
        b"\x00\x00\xFF\xFF"  # blue
        b"\xFF\xFF\xFF\xFF"  # white
    )

    output_image_data, output_palette = imagequant.quantize_raw_rgba_bytes(
        IMAGE_DATA,  # RGBA image data
        2, 2,        # width, height
        dithering_level=1.0,
        max_colors=256,
    )

    # you can now encode image data and the palette in any image format...

Example ``output_image_data``:

.. code-block:: python

    b'\x02\x03\x00\x01'

Example ``output_palette``:

.. code-block:: python

    [0, 0, 255, 255, 255, 255, 255, 255, 255, 0, 0, 255, 0, 255, 0, 255, 0, 0, 0, 0, ...]
    # color 0      | color 1           | color 2       | color 3       | color 4   | ...


License
-------

**Imagequant Python** is licensed under the BSD 3 Clause. See the LICENSE_ file for more information.

**Libimagequant** is dual-licensed:

* For Free/Libre Open Source Software it's available under GPL v3 or later with additional copyright notices for older parts of the code.

* For use in closed-source software, AppStore distribution, and other non-GPL uses, you can obtain a commercial license.

Read its `license terms <https://github.com/ImageOptim/libimagequant#license>`_ for more information.

.. _LICENSE: ./LICENSE
