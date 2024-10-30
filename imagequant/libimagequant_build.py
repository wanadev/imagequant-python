import os

from cffi import FFI
from distutils import ccompiler


_ROOT = os.path.abspath(os.path.dirname(__file__))
_LIBIMAGEQUANT_H = os.path.join(_ROOT, "libimagequant.h")
_LIBIMAGEQUANT_SRC = [
    "blur.c",
    "kmeans.c",
    "mediancut.c",
    "mempool.c",
    "nearest.c",
    "pam.c",
    "libimagequant.c",
]

CC_ARGS = []
if ccompiler.get_default_compiler() == "unix":
    CC_ARGS = ["-Wno-incompatible-pointer-types"]


ffibuilder = FFI()
ffibuilder.set_source(
    "imagequant._libimagequant",
    "\n".join(['#include "%s"' % c for c in _LIBIMAGEQUANT_SRC]),
    include_dirs=[
        os.path.join(_ROOT, "..", "libimagequant"),
    ],
    extra_compile_args=CC_ARGS,
)
ffibuilder.cdef(open(_LIBIMAGEQUANT_H, "r").read())


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
