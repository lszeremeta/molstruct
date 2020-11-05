#!/usr/bin/env python
"""The setup script."""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="molstruct",
    version="2.0.1",
    author="Łukasz Szeremeta",
    author_email="l.szeremeta.dev+molstruct@gmail.com",
    license="MIT License",
    description="Convert chemical molecule data CSV files to structured data formats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lszeremeta/molstruct",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing :: Markup",
        "Topic :: Utilities"
    ],
    keywords=[
        "Molstruct",
        "cheminformatics",
        "parser",
        "CLI",
        "CSV",
        "structured data",
        "JSON-LD",
        "JSON",
        "Microdata",
        "RDFa",
        "MolecularEntity",
        "molecules",
        "converter",
        "Bioschemas",
        "schema.org",
        "chemical data"
    ],
    python_requires='>=3.2',
    entry_points={
        "console_scripts": [
            "molstruct=molstruct.__main__:main",
        ]
    }
)
