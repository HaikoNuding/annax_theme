#######
WEB2PDF
#######

.. _WEB2PDF:

- Introduction
- Functionality

WEB2PDF
=======

The web2pdf is a simple python script which will generate a pdf document
from the generated sphinx documentation.

Generate a PDF file with the default file name:

.. code:: console

    $ python3 web2pdf

Generate a PDF file with the given file name:

.. code:: console

    $ python3 web2pdf -pdf AnnaxDoc1

Functionality
=============

* First open the index.html file, to extract all necessary data
* Create a BeautifulSoup object, which represents the document as a nested data structure.
* Get all HTML files inside a list.
* Create using pdfkit the pdf document.