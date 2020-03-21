# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
#import os
#import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- yueshen add  -----------------------------------------------------
# # If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import sys
import os
from subprocess import run

current_run_path=os.getcwd()
sphinx_project_path=os.path.abspath('..')
sphinx_source_path=os.path.dirname(os.path.abspath(__file__))

if  os.path.exists(".extensions"):
    sys.path.insert(0, os.path.abspath('.'))
    sys.path.insert(1, os.path.abspath('.extensions'))
    print("system path env is: \n" + str(sys.path))
else:
    print("can't add extensions into path env")
# ---------------------------------------------------------

import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

try:
    import sphinxcontrib.plantuml
    import sphinxcontrib.openapi
except ImportError:
    pipInstallCmd = ['sh','../requirement.sh']
    run(pipInstallCmd)
    #subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd = sphinx_source_path )
    pass

extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.graphviz',
    'sphinx.ext.extlinks',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.openapi',
    'doors.doors',
    'pdf_export'
]


'''
from recommonmark.parser import CommonMarkParser
source_parsers = {
    '.md': CommonMarkParser,
}
'''

# ---------------------------------------------------------
#locate index.rst, otherwise sphinx may find contents.rst as default
master_doc = 'index'

source_suffix = ['.rst', '.md']

todo_include_todos=True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = False
highlight_language = 'cpp'
# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '.static/logo.png'

# -- Project information -----------------------------------------------------

project = 'cleanMind'
copyright = '2020, yueshen'
author = 'yueshen'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = [
#]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['.static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'


# -- PlantUML configuration ------------------------------------------------

path = os.path.abspath('.extensions/plantuml.jar')
path = path.replace("\\","/")

plantuml = 'java -jar %s' % path

plantuml_output_format = 'svg'
