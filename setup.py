import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="honorifics-tloc",
    version="0.0.1",
    author="Animagia.pl",
    author_email="animagia@animagia.pl",
    description="Swaps terms in ass subtitles, good for Japanese honorifics.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Animagia/honorifics",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'honorifics = honorifics.honorifics:main_func',
        ]
    }
)
