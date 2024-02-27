#!/usr/bin/env python3

import os
from setuptools import setup, find_namespace_packages

VERSION_FILE = os.path.join(os.path.dirname(__file__), "VERSION.txt")

setup(
    name="mtopengl",
    description="Minh-Tri Pham's extra modules for dealing with OpenGL in Python",
    author=["Minh-Tri Pham"],
    packages=find_namespace_packages(include=["mt.*"]),
    # scripts=[
    #     "scripts/immview",
    # ],
    install_requires=[
        "pyopengl",
        "glfw",
        "mtglm",
        # "mtbase>=4.25",  # we don't need mtbase yet
    ],
    setup_requires=["setuptools-git-versioning<2"],
    setuptools_git_versioning={
        "enabled": True,
        "version_file": VERSION_FILE,
        "count_commits_from_version_file": True,
        "template": "{tag}",
        "dev_template": "{tag}.dev{ccount}+{branch}",
        "dirty_template": "{tag}.post{ccount}",
    },
)
