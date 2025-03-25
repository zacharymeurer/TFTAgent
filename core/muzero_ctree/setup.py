from setuptools import setup
from Cython.Build import cythonize
import numpy as np

from setuptools.extension import Extension

extensions = [
    Extension(
        "cytree",
        ["cytree.pyx"],
        extra_compile_args=["-O3", "-std=c++20"],  # Add -std=c++20 here
        include_dirs=[np.get_include()],
        language="c++",  # Ensure Cython compiles with C++
    )
]

setup(ext_modules=cythonize(extensions))

# Might be able to remove extra_compile_args, leaving in until I have better information
#setup(ext_modules=cythonize('cytree.pyx'), extra_compile_args=['-O3'], include_dirs=[np.get_include()])
