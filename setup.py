#!/usr/bin/env python3

from setuptools import setup, find_packages
from secretum import __version__
import os

try:
    long_description = open("README.md", "r").read()
except Exception as e:
    long_description = "Complex password generator"


def read_requirements():
    requirements_path = os.path.join(".", "requirements.txt")
    with open(requirements_path, "r") as f:
        requirements = [line.strip() for line in f]

    return requirements


setup(
    name="secretum",
    version=__version__,
    description="Complex password generator",
    long_description=long_description,
    author="Jalil SA",
    url="https://github.com/jxlil/secretum",
    packages=find_packages(),
    scripts=["bin/secretum"],
    install_requires=read_requirements(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
    ],
)
