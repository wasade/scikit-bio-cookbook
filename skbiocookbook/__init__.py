#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2013--, scikit-bio development team.
#
# Distributed under the terms of the Creative Commons Attribution-
# NonCommercial-ShareAlike 4.0 International License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

from glob import glob
from os.path import splitext

__version__ = "0.0.0-dev"

def cookbook_toc():
    """Generate HTML string of the scikit-bio Cookbook Table of Contents
    """
    toc = ["<h2>Table of Contents</h2><p>"]
    nb_paths = [fp for fp in glob('*.ipynb') if fp != "Index.ipynb"]
    for nb_path in nb_paths:
        title = ' '.join(splitext(nb_path)[0].split('-'))
        toc.append("<li><a href='%s'  target='_blank'>%s</a></li>" % \
            (nb_path, title.title()))

    return '\n'.join(toc)
