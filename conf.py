# basedir is set by <lang>/conf.py
"""
Use "-D language=<LANG>" option to build a localized felupe-docs document.

For example::

    sphinx-build -D language=ja -b html . _build/html

This conf.py do:

- Specify `locale_dirs` and `gettext_compact`.
- Overrides source directory as 'mayavi/docs/source/mayavi`.

"""
from pathlib import Path

basedir = Path(__file__).resolve().parent / "mayavi/docs/source/mayavi"
exec((basedir / "conf.py").read_text(), globals())  # noqa: S102

locale_dirs = [basedir / "../../../../locale/"]


def setup(app):  # noqa: D103,ANN001,ANN201
    from sphinx.ext.autodoc import cut_lines

    app.srcdir = Path(basedir)
    app.confdir = Path(app.srcdir)
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
