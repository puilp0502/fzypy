from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [
    Extension("fzy.choices", ["fzy/choices.pyx"], define_macros=[("VERSION", '"1.0"')])
]
setup(ext_modules=cythonize(extensions))
