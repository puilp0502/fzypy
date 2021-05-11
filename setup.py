from setuptools import Extension, setup, find_packages
from setuptools.command.build_ext import build_ext as _build_ext
from warnings import warn
import os.path
import shutil
from Cython.Build import cythonize


VERSION = "0.0.2-a1"
FZY_VERSION = "1.0"  # TODO Parse from Makefile?

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


def copy_fzy_config(fzy_root):
    # TODO Parse from Makefile?
    config_src = os.path.join(fzy_root, "src/config.def.h")
    config_dest = os.path.join(fzy_root, "config.h")

    if not os.path.exists(config_dest):
        try:
            shutil.copyfile(config_src, config_dest)
        except FileNotFoundError:
            warn(
                'fzy config definition ("{}") was not found. '.format(config_src)
                + "Ensure that the git submodules are initialized."
            )
        except OSError:
            pass


class build_ext(_build_ext):
    def run(self):
        setup_py_root = os.path.dirname(os.path.abspath(__file__))
        copy_fzy_config(os.path.join(setup_py_root, "fzy"))
        super().run()


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="fzypy",
    version=VERSION,
    author="Frank Yang",
    author_email="puilp0502@gmail.com",
    description="A fuzzy finder in Python based on fzy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/puilp0502/fzypy",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    cmdclass={
        "build_ext": build_ext,
    },
    ext_modules=cythonize(extensions, include_path=include_path),
)
