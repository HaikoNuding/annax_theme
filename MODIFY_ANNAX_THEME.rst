##################
Modify Annax Theme
##################

.. _Modify-Annax-Theme:

- Theme structure
- Theme style changes
- Theme configuration
- Theme static files

Annax Theme structure
=====================

::

    annax_theme
    ├── annax_theme
    ├── annax_theme.egg-info
    ├── bin
    ├── docs
    ├── node_modules
    ├── sphinx_rtd_theme.egg-info
    ├── src
    └── tests

Theme style changes
===================

The Annax theme pulls from other frontend projects.
The only styles you should edit are the sass files that start with "theme_*.sass".

Changes must be done according to the sass structure.

.. note::
    The sass files are located in the ``src`` directory.

How to use SASS
---------------

Sass is a stylesheet language that is compiled to CSS.
It allows you to use ``variables``, ``nested rules``, ``mixins``, ``functions`` and more.

Sass supports two different syntax's SCSS and The Indented Syntax.
The indented syntax was Sass's original syntax and so it uses the file extension ``*.sass``.


Theme configuration
===================

The ``theme.conf`` contains theme settings including options.
By using the Django template language the theme options variables can be used with ``theme_*variable_name`` in theme HTML.

The theme options can also be changed in the Sphinx configuration file for the Sphinx documentation builder ``config.py``.

Theme static files
==================

::

    annax_theme
    ├── annax_theme
    │    ├── locale
    │    ├── __pycache__
    │    ├── static
    │        ├── css
    │        │   └── fonts
    │        ├── images
    │        ├── js
    ├── annax_theme.egg-info
    ├── bin
    ├── docs
    ├── node_modules
    ├── sphinx_rtd_theme.egg-info
    ├── src
    └── tests

.. note::

    The static folder contains the final static files.