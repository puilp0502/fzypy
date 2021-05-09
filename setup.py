from setuptools import Extension, setup, find_packages
from Cython.Build import cythonize

VERSION = "0.0.1"
FZY_VERSION = "1.0"

include_path = ["src/fzy/"]
extensions = [
    Extension(
        "fzy.choices",
        ["src/fzy/choices.pyx"],
        define_macros=[("VERSION", '"{}"'.format(FZY_VERSION))],
    ),
    Extension(
        "fzy.match",
        ["src/fzy/match.pyx"],
        define_macros=[("VERSION", '"{}"'.format(FZY_VERSION))],
    ),
]

setup(
    name="fzy",
    version="{}-{}".format(VERSION, FZY_VERSION),
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    ext_modules=cythonize(extensions, include_path=include_path),
)
