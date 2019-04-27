# BASEDIR is set by <lang>/conf.py
"""
Use "-D language=<LANG>" option to build a localized mayavi document.
For example::

    sphinx-build -D language=ja -b html . _build/html

This conf.py do:

- Specify `locale_dirs` and `gettext_compact`.
- Overrides source directory as 'mayavi/docs/source/mayavi`.

"""
import os
from sphinx.util.pycompat import execfile_

BASEDIR = os.path.dirname(os.path.abspath(__file__))

os.chdir('mayavi/docs/source/mayavi')
execfile_(os.path.join(BASEDIR, 'mayavi/docs/source/mayavi/conf.py'), globals())

locale_dirs = [os.path.join(BASEDIR, 'locale/')]
gettext_compact = False

setup_original = setup  # from 'mayavi/docs/source/mayavi/conf.py'

def setup(app):
    app.srcdir = os.path.join(BASEDIR, 'mayavi/docs/source/mayavi/')
    app.confdir = app.srcdir

    setup_original(app)
