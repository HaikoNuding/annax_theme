******************
Annax Sphinx Theme
******************

.. image:: https://img.shields.io/pypi/v/sphinx_rtd_theme.svg
   :target: https://pypi.python.org/pypi/sphinx_rtd_theme
   :alt: Pypi Version
.. image:: https://travis-ci.org/readthedocs/sphinx_rtd_theme.svg?branch=master
   :target: https://travis-ci.org/readthedocs/sphinx_rtd_theme
   :alt: Build Status
.. image:: https://img.shields.io/pypi/l/sphinx_rtd_theme.svg
   :target: https://pypi.python.org/pypi/sphinx_rtd_theme/
   :alt: License
.. image:: https://readthedocs.org/projects/sphinx-rtd-theme/badge/?version=latest
   :target: http://sphinx-rtd-theme.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

This Sphinx_ theme is based on the `Read the Docs`_ theme. The Annnax theme
was designed to satisfy the Annax documentation requirements.

.. _Sphinx: http://www.sphinx-doc.org
.. _Read the Docs: http://www.readthedocs.org

************
Installation
************

Install from tar.gz
===================

You can install the ``annax_theme-0.5.0.tar.gz``, by following these steps:

.. code:: console

    $ tar -xzf annax_theme-0.5.0.tar.gz
    $ cd annax_theme-0.5.0

Set up your environment
=======================

Install Sphinx and documentation build dependencies

.. code:: console

    $ pip3 install -e '.[dev]'

Install Sphinx Webpack, node-sass and the the dependencies locally.

.. code:: console

    $ npm install

Making changes
==============

Changes to the ``annnax theme`` can be tested with Webpack:

.. code:: console

    $ npm run dev

This script will do the following:

* Install and update any dependencies.
* Build the static CSS from SASS source files.
* Build the demo documentation.
* Build the demo documentation.
* Watch for changes to the SASS files and documentation and rebuild everything on any detected changes.

Alternatively, if you dont need to watch the files, the release build can be used to test built assets:

.. code:: console

    $ npm run build


Switch to annax theme
=====================

To use the theme in your Sphinx project, you will need to add the following to
your ``conf.py`` file:

.. code:: python

    import annax_theme

    extensions = [
        ...
        "annax_theme",
    ]

    html_theme = "annax_theme"

For more information read the full documentation on `installing the theme`_

.. _PyPI: https://pypi.python.org/pypi/sphinx_rtd_theme
.. _installing the theme: https://sphinx-rtd-theme.readthedocs.io/en/latest/installing.html

Configuration
=============

This theme is highly customizable on both the page level and on a global level.
To see all the possible configuration options, read the documentation on
`configuring the theme`_.

.. _configuring the theme: https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html

Generate PDF documentation
==========================

The Annax Sphinx Theme offers a python script which will generate a pdf document from the
Annax Sphinx documentation. The default PDF file name is the project name.

::

    annax_theme
    ├── annax_theme
    │    ├── locale
    │    ├── __pycache__
    │    ├── static
    │        ├── css
    │        ├── images
    │        ├── js
    │        ├── tools
    │        │   └── ``web2pdf.py``
    ├── annax_theme.egg-info
    ├── bin
    ├── docs
    ├── node_modules
    ├── sphinx_rtd_theme.egg-info
    ├── src
    └── tests

Generate a PDF file with the default file name:

.. code:: console

    $ python3 web2pdf

Generate a PDF file with the given file name:

.. code:: console

    $ python3 web2pdf -pdf AnnaxDoc1

For more information, read the full documentation on our :ref:`WEB2PDF` documentation.

Contributing
============

If you would like to help modify or translate the theme, you'll find more
information on contributing in our `contributing guide`_.

.. _contributing guide: https://sphinx-rtd-theme.readthedocs.io/en/latest/contributing.html

Modifying the theme
===================

The styles for this theme use `SASS`_ and a custom CSS framework called `Wyrm`_.
We use `Webpack`_ and `node-sass`_ to build the CSS.
More information for modifying the Annax theme in :ref:`Modify-Annax-Theme`.

.. _SASS: http://www.sass-lang.com/
.. _Wyrm: https://github.com/snide/wyrm/
.. _Webpack: https://webpack.js.org/
.. _node-sass: https://github.com/sass/node-sass