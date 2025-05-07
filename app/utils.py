import pdfplumber
import pytesseract
from PIL import Image
import os
from pdf2image import convert_from_path
from pathlib import Path

OUTPUT_LOCATION = "auto-tc_pdf_converter_output"


def get_local_save_path(file_name):
    dir = os.path.join(os.path.expanduser("~"), "Documents", OUTPUT_LOCATION)
    if not os.path.isdir(dir):
        os.mkdir(dir)
    return os.path.join(dir, file_name)


def convert_pages_to_images(path):
    """Loops through the pages in PDF at provided path and outputs them as indivudual high-quality JPEG images"""
    pages = convert_from_path(path, 350)
    i = 1
    for page in pages:
        image_name = f"Page_{str(i)}.jpg"
        page.save(get_local_save_path(image_name), "JPEG")
        i += 1
        

repo_root = Path(__file__).parents[1]
pdf_path = repo_root.joinpath('docs/F201 - Purchase and Sale Agreement test.pdf')

convert_pages_to_images(pdf_path)