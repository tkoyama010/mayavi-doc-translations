# basedir is set by <lang>/conf.py
"""
Use "-D language=<LANG>" option to build a localized mayavi document.
For example::

    sphinx-build -D language=ja -b html . _build/html

This conf.py do:

- Specify `locale_dirs` and `gettext_compact`.
- Overrides source directory as 'mayavi/docs/source/mayavi`.

"""
import os
import pathlib

basedir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "mayavi/docs/source/mayavi"
)
exec(pathlib.Path(os.path.join(basedir, "conf.py")).read_text(), globals())

locale_dirs = [os.path.join(basedir, "../../../../locale/")]


def setup(app):
    from sphinx.ext.autodoc import cut_lines

    app.srcdir = pathlib.Path(basedir)
    app.confdir = pathlib.Path(app.srcdir)
    app.connect("autodoc-process-docstring", cut_lines(4, what=["module"]))
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
    )

    # workaround for RTD
    from sphinx.util import logging

    logger = logging.getLogger(__name__)
    app.info = lambda *args, **kwargs: logger.info(*args, **kwargs)
    app.warn = lambda *args, **kwargs: logger.warning(*args, **kwargs)
    app.debug = lambda *args, **kwargs: logger.debug(*args, **kwargs)
