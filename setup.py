#!/usr/bin/env python3

from setuptools import setup, find_namespace_packages
from mt.opengl.version import version

setup(
    name="mtopengl",
    version=version,
    description="Minh-Tri Pham's extra modules for dealing with OpenGL in Python",
    author=["Minh-Tri Pham"],
    packages=find_namespace_packages(include=["mt.*"]),
    # scripts=[
    #     "scripts/immview",
    # ],
    install_requires=[
        "pyglm",
        "pyopengl",
        "glfw",
        "mtbase>=4.25",
    ],
)
