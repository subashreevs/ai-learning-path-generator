# utils/pdf_parser.py
from pypdf import PdfReader

def extract_text_from_pdf(file_obj):
    reader = PdfReader(file_obj)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"
    return text