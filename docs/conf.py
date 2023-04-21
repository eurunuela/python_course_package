#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# python_course documentation build configuration file, created by
# sphinx-quickstart
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime  # access current time and date
from distutils.version import LooseVersion

import sphinx
import sphinx_rtd_theme

import python_course

sys.path.insert(0, os.path.abspath("sphinxext"))
sys.path.insert(0, os.path.abspath(os.path.pardir))

from github_link import make_linkcode_resolve

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.

# needs_sphinx = '1.0'

# generate autosummary even if no references
autosummary_generate = True
add_module_names = False

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "matplotlib.sphinxext.plot_directive",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.ifconfig",
    "sphinx.ext.intersphinx",
    "sphinx.ext.linkcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
]

if LooseVersion(sphinx.__version__) < LooseVersion("1.4"):
    extensions.append("sphinx.ext.pngmath")
else:
    extensions.append("sphinx.ext.imgmath")

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.

project = "python_course"
copyright = "2021-" + datetime.today().strftime("%Y") + ", python_course Developers"
author = "python_course Developers"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The short X.Y version.
version = python_course.__version__
# The full version, including alpha/beta/rc tags.
release = python_course.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -----------------------------------------------------------------------------
# Napoleon settings
# -----------------------------------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = False
napoleon_use_keyword = True
napoleon_use_rtype = False

# -----------------------------------------------------------------------------
# nbsphinx settings
# -----------------------------------------------------------------------------
nbsphinx_execute = "never"

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# installing theme package
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "includehidden": False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


def setup(app):
    """Add CSS/JS extensions.

    Notes
    -----
    From https://github.com/rtfd/sphinx_rtd_theme/issues/117
    """
    app.add_css_file("theme_overrides.css")
    app.add_js_file("zenodo.js")


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "python_coursedoc"

# The following is used by sphinx.ext.linkcode to provide links to github
linkcode_resolve = make_linkcode_resolve(
    "python_course",
    "https://github.com/python_course/python_course/blob/{revision}/{package}/{path}#L{lineno}",
)

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference/", None),
    "matplotlib": ("https://matplotlib.org/", None),
    "nibabel": ("https://nipy.org/nibabel/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "nilearn": ("http://nilearn.github.io/", None),
}
