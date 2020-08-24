import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="molstruct", # Replace with your own username
    version="1.0.11",
    author="Łukasz Szeremeta",
    author_email="l.szeremeta.dev@gmail.com",
    description="Convert chemical molecule data CSV files to structured data formats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lszeremeta/molstruct",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.2',
    entry_points={
        "console_scripts": [
            "molstruct=molstruct.__main__:main",
        ]
    }
)