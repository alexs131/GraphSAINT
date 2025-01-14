# cython: language_level=3
from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy
# import cython_utils

import os
os.environ["CC"] = "/opt/homebrew/Cellar/gcc/11.2.0_3/bin/g++-11"
os.environ["CXX"] = "/opt/homebrew/Cellar/gcc/11.2.0_3/bin/g++-11"

setup(ext_modules=cythonize(["graphsaint/cython_sampler.pyx", "graphsaint/cython_utils.pyx",
      "graphsaint/norm_aggr.pyx"]), include_dirs=[numpy.get_include()])
# to compile: python graphsaint/setup.py build_ext --inplace
