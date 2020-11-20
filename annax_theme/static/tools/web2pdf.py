import pdfkit
import codecs

import requests
from bs4 import BeautifulSoup
import urllib.parse
from pathvalidate import sanitize_filename

# The index file must be the first page of the pdf, since this is the table of contents.
FILE_PATHS = ['../../index.html']

# pdfkit pdf file options
options = {
    'page-size': 'A4',
    "disable-local-file-access": None,
    "enable-local-file-access": None,
    'javascript-delay': '20000',
    "print-media-type": None,
    'footer-right': '[page]',
    'disable-smart-shrinking': None
}

# Open index.html file to extract all necessary data.
file = codecs.open('../../index.html', "r", "utf-8")

# BeautifulSoup object 'soup' represents the document as a nested data structure
soup = BeautifulSoup(file, "html.parser")

# Read documentation title from HTML and use it as PDF name.
DOCUMENT_TITLE = sanitize_filename(soup.select('title',)[0].text.strip())

# Create a list with all documentation HTML files
for ul_tag in soup.find_all('ul'):
    for li_tag in ul_tag.find_all('li', {'class': 'toctree-l1'}):
        for a_tag in li_tag.find_all('a', {'class': 'reference internal'}):
            if a_tag.get('href') is not None and a_tag.get('href').endswith("html"):
                file_path = urllib.parse.unquote(a_tag.get('href'))
                print("./" + file_path)
                FILE_PATHS.append('./../../'+file_path)

# Remove duplicates
FILE_PATHS = list(dict.fromkeys(FILE_PATHS))

# Create PDF file with pdfkit.
pdfkit.from_file(FILE_PATHS, './../../' + DOCUMENT_TITLE, options=options)
