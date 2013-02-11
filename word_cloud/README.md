copied from https://github.com/amueller/word_cloud to address issues with PIL import

## What's changed from original script

- Import PIL in better way (it depends on installations)
- Use font from this project as default
- Added option to redraw in color (by default is `True` as in original)

## Original README

word cloud
==========

A little word cloud generator in Python.

Needs PIL, numpy and Cython (``>= 0.16``).

The example uses scikit-learn for extracting word counts from a text.
For scikit-learn ``<= 0.11``, you have to remove the ``min_df`` keyword.

Build using ``make`` or ``python setup.py build_ext -i``.

See my blog for some details:
http://peekaboo-vision.blogspot.de/2012/11/a-wordcloud-in-python.html

For the blog post I removed the word ``shall`` from the constitution word count
which is not in the scikit-learn stopword list.
