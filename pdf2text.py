import pandas as pd
import numpy as np
import string
import os, io

from pathlib import Path
import requests
    
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def get_pdf_from_url(save_path, pdf_url):
    pdf = Path(save_path)
    response = requests.get(pdf_url)
    pdf.write_bytes(response.content)
    
def pdf_info(pdf_path):
    pdf = open(pdf_path, 'rb')
    parser = PDFParser(pdf)
    return PDFDocument(parser).info[0]

def pdf2txt(pdf_path):
    
    pdf = open(pdf_path, 'rb')

    # Init.
    resource_manager = PDFResourceManager()
    string_buffer = io.StringIO()  
    
    # Construct.
    converter = TextConverter(resource_manager, 
                              string_buffer, 
                              laparams=LAParams(), 
                              codec='utf-8')
    interpreter = PDFPageInterpreter(resource_manager, converter) 
    
    # Read pdf (list of pages).
    pdf_pages = PDFPage.get_pages(pdf, check_extractable=True) # list
    
    # Process pdf to text.
    [interpreter.process_page(page) for page in pdf_pages]
    
    # Result.
    pdf_text = string_buffer.getvalue()
    
    [o.close() for o in [pdf, string_buffer, converter]]
    return pdf_text