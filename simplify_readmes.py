#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import re, sys, string
from bs4 import BeautifulSoup
from markdown import markdown
from docutils import core
from docutils.writers.html4css1 import Writer, HTMLTranslator
from os import listdir
from os.path import isfile, join

reload(sys)  
sys.setdefaultencoding('utf8')

READMES_DIR = "./READMES"
TEXT_DIR = "./TEXT"

non_decimal = re.compile(r'[^\d.]+')

class HTMLFragmentTranslator( HTMLTranslator ):
    def __init__( self, document ):
        HTMLTranslator.__init__( self, document )
        self.head_prefix = ['','','','','']
        self.body_prefix = []
        self.body_suffix = []
        self.stylesheet = []
    def astext(self):
        return ''.join(self.body)

html_fragment_writer = Writer()
html_fragment_writer.translator_class = HTMLFragmentTranslator

def markdown_to_html(markdown_string):
    # md -> html -> text since BeautifulSoup can extract text cleanly
    html = markdown(markdown_string)

    # remove code snippets
    html = re.sub(r'<pre>(.*?)</pre>', ' ', html)
    html = re.sub(r'<code>(.*?)</code >', ' ', html)

    return html

def html_to_text(html):
    # extract text
    soup = BeautifulSoup(html, "html.parser")
    text = ''.join(soup.findAll(text=True))

    return " ".join(text.split())

def markdown_to_text(markdown_string):
    """ Converts a markdown string to plaintext """
    return html_to_text(markdown_to_html(markdown_string))

def reST_to_html(rst_text):
    return core.publish_string(rst_text, writer = html_fragment_writer)

def rst_to_text(rst_text):
    return html_to_text(reST_to_html(rst_text))

def standardize(text):
    return " ".join(re.sub("/[^ \w]+/", "", re.sub('['+string.punctuation+']', ' ', text.strip().lower() )).split())

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

READMES = sorted([f for f in listdir(READMES_DIR) if isfile(join(READMES_DIR, f))])

print("%d files to convert" % len(READMES))

MARKDOWN_EXTENSIONS = [ "md", "markdown", "mdown" ]

UNIQUE_EXTENSIONS = set()
EXTENSION_COUNT = { '' : 0, 'md' : 0, 'markdown' : 0, 'mdown' : 0, 'html' : 0, 'rst' : 0, 'txt' : 0 }

size_ratios = [ ]
out_files = 0

for README in READMES:
    file_parts = README.split('.')
    ext = file_parts[-1].lower()

    UNIQUE_EXTENSIONS.add(ext)
    EXTENSION_COUNT[ext] += 1

    read_file_name = READMES_DIR + "/" + README
    with open(read_file_name, "r") as read_file:
        contents = read_file.read()
        in_size = len(contents)
        print("Reading <%s> (%d)" % (read_file_name, in_size))
        
        # remove apostrophes from concatenated words
        contents = contents.replace("’", "").replace("'", "")
        out_text = ""

        if ext is 'html':
            out_text = standardize(html_to_text(contents))
        elif ext is 'rst':
            out_text = standardize(rst_to_text(contents))
        elif ext in MARKDOWN_EXTENSIONS:
            out_text = standardize(markdown_to_text(contents))
        
        out_size = len(out_text)
        if out_size > 0:
            write_file_name = TEXT_DIR + "/" + README
            with open(write_file_name, "w") as write_file:
                write_file.write(out_text)
                write_file.close()
                print("Wrote <%s> (%d)" % (write_file_name, out_size))
                size_ratios.append(float(100 * out_size / in_size))
                out_files += 1

print("Average filesize change (%d)" % mean(size_ratios))
print(UNIQUE_EXTENSIONS)
print(EXTENSION_COUNT)
