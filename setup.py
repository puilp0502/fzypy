from setuptools import Extension, setup, find_packages
from setuptools.command.build_ext import build_ext as _build_ext
from warnings import warn
import os.path
import shutil
from Cython.Build import cythonize

VERSION = "0.0.1"
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


setup(
    name="fzy",
    version="{}+{}".format(VERSION, FZY_VERSION),
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    cmdclass={
        "build_ext": build_ext,
    },
    ext_modules=cythonize(extensions, include_path=include_path),
)
