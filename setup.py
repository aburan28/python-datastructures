from distutils.core import setup, Extension
import numpy
from Cython.Distutils import build_ext

setup(
	cmdclass={'build_ext': build_ext},
	ext_modules=[Extension("python-datastructures",
		sources=[".pyx", ".c"],
		)

