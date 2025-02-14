# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import polysolve
from datetime import date

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'polysolve'
copyright = '2025, Rhea'
author = 'polysolve.__author__'
release = 'polysolve.__version__'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
"sphinx.ext.autodoc",
"sphinx.ext.napoleon",
"sphinx.ext.autosummary",
"sphinx_autodoc_typehints",
"sphinx.ext.intersphinx",
]

#intersphinx_mapping = {'python':(https://docs.python.org/3/...}

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
