![An example output produced with fullGridMinimal.](outputs/waves.svg)

# wang-tiles [![Python 3.6](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/downloads/)

Some experiments with using [Wang Tiles](https://en.wikipedia.org/wiki/Wang_tile) to generate continuous unicode terrains or, at least, nice SVGs.

## Usage

`wang-tiles` requires some version of Python 3.

**Install requirements:** `make install`

As I've only been playing around with configurations, these files are ill-designed for import and use in other Python scripts. I typically modify the helper functions available in `experiments.py`and mess around in the Python REPL to produce grids.

**Mess around in the REPL:** `make repl`

## Notes

One set of unicode-printable tiles produced a Sierpinski triangle of its own accord; that lives in the `outputs` directory, along with any other interesting output I find along the way.

The color scheme of the wavy image above is an attempt at combination #281 of Wada Sanzō's [*A Dictionary of Color Combinations*](http://www.ampersandgallerypdx.com/books/dictionary-of-color-combinations-sanzo-wada): Antwarp Blue, Benzol Green, Pale Lemon Yellow, and Cobalt Green.
