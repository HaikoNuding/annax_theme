import argparse
import os
import pdfkit
import codecs
from bs4 import BeautifulSoup
import urllib.parse
from natsort import natsort
from pathvalidate import sanitize_filename
import os.path as op

# Add python file arguments
parser = argparse.ArgumentParser(description='PDF file name')
parser.add_argument('-pdf', '--pdf_name', metavar='', required=False, type=str, help='PDF file name')
parser.add_argument('-r', '--r', required=False, type=bool, help='Generate from HTML directory')
args = parser.parse_args()

# The index file must be the first page of the pdf, since this is the table of contents.
FILE_PATHS = {}
DOCUMENT_TITLE = None
BUILD_DIR = op.abspath(op.join(__file__, op.pardir, op.pardir, op.pardir, op.pardir))
SINGLE_HTML_INDEX_PATH = os.path.join(BUILD_DIR, "singlehtml", "index.html")
HTML_INDEX_PATH = os.path.join(BUILD_DIR, "html", "index.html")


# pdfkit pdf file options
# https://wkhtmltopdf.org/usage/wkhtmltopdf.txt
options = {
    '--header-html': './header.html',
    '--footer-html': './footer.html',
    'page-size': 'A4',
    "disable-local-file-access": None,
    "enable-local-file-access": None,
    'javascript-delay': '20000',
    'disable-smart-shrinking': None,
    '--header-spacing': 10,
    '--footer-spacing': 10,
    '--margin-left': "15mm",
    '--margin-right': "15mm",
    '--margin-top': "38mm",
    '--margin-bottom': "38mm",
    '--images': None,
    '--allow': BUILD_DIR+'/html/_images',
    '--image-dpi': 360,
    'print-media-type': None

}

print(BUILD_DIR+'/html/_images')
# table of content style
toc = {
    'xsl-style-sheet': 'toc.xsl',

}

cover = './title_page_default.html'


# Create a list with all documentation HTML files
def get_file_paths_of(soup, soup_head):
    for ul_tag in soup.find_all('ul'):
        for li_tag in ul_tag.find_all('li'):
            for a_tag in li_tag.find_all('a', {'class': 'reference internal'}):
                if a_tag.get('href') is not None and a_tag.get('href').endswith("html"):
                    file_path = urllib.parse.unquote(a_tag.get('href'))
                    file_key = urllib.parse.unquote(a_tag.text)
                    head, tail = os.path.split(file_path)
                    norm_path = os.path.normpath(head)
                    if soup_head != " ":
                        norm_path = os.path.normpath(head)
                        file_path = soup_head + file_path
                    else:
                        file_path = './../../' + file_path
                    if file_path not in list(FILE_PATHS.values()) and not norm_path.startswith("..") and not soup_head.startswith(".."):
                        FILE_PATHS[str(file_key)] = file_path


def generate_pdf_from(index_soup):
    get_file_paths_of(index_soup, " ")
    for file_path in list(FILE_PATHS.values()):
        f = codecs.open(file_path, "r", "utf-8")
        head, tail = os.path.split(file_path)
        head = head + "/"
        s = BeautifulSoup(f, "html.parser")
        get_file_paths_of(s, head)


def get_document_title(index_soup):
    # Use pdf name argument if set.
    if args.pdf_name is None:
        # Read documentation title from HTML and use it as PDF name.
        title = sanitize_filename(index_soup.select('title', )[0].text.strip())
    else:
        title = args.pdf_name
    return title


def single_html_exists():
    # Open index.html file to extract all necessary data.
    if os.path.isfile(SINGLE_HTML_INDEX_PATH):
        return True
    else:
        return False


def create_pdf():
    global FILE_PATHS
    global DOCUMENT_TITLE
    if single_html_exists() and args.r is None:
        print("Generating pdf from single html directory.")
        FILE_PATHS = {"1": SINGLE_HTML_INDEX_PATH}
        index_file = codecs.open(SINGLE_HTML_INDEX_PATH, "r", "utf-8")
        index_soup = BeautifulSoup(index_file, "html.parser")
    else:
        print("Generating pdf from read html directory.")
        index_file = codecs.open(HTML_INDEX_PATH, "r", "utf-8")
        index_soup = BeautifulSoup(index_file, "html.parser")
        generate_pdf_from(index_soup)
    # Get title of the pdf
    DOCUMENT_TITLE = get_document_title(index_soup)


create_pdf()

FILE_PATHS = natsort.natsorted(FILE_PATHS.items())

FILE_PATHS = dict(FILE_PATHS)

# Create PDF file with pdfkit.
pdfkit.from_file(list(FILE_PATHS.values()), './../../' + DOCUMENT_TITLE + '.pdf', options=options, toc=toc, cover=cover, cover_first=True)
