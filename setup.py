#!/usr/bin/env python
import os

from setuptools import find_packages, setup

STUBS_FOR = "factory_boy"
PACKAGE_NAME = f"{STUBS_FOR}-stubs"


def find_stub_files() -> list[str]:
    """
    Collect all .pyi files in the package directory.
    """
    result = []
    for root, _, files in os.walk(PACKAGE_NAME):
        for file in files:
            if file.endswith(".pyi"):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
    return result


with open("README.md", encoding="utf-8") as f:
    readme = f.read()

dependencies = [STUBS_FOR]

setup(
    name=PACKAGE_NAME,
    version="0.0.1",
    description=f"Mypy stubs for {STUBS_FOR}",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MIT",
    license_files=["LICENSE.md"],
    url=f"https://github.com/Elbtalkessel/{PACKAGE_NAME}",
    author="Elbtalkessel",
    author_email="rtfsc@pm.me",
    py_modules=[],
    python_requires=">=3.8",
    install_requires=dependencies,
    packages=[PACKAGE_NAME, *find_packages()],
    package_data={
        PACKAGE_NAME: find_stub_files(),
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Typing :: Typed",
    ],
)
