import os
from pypdf import PdfReader
from pathlib import Path
import pdfplumber
import pytesseract

def extract_pdf_data(file: str) -> dict[str, str]:
    with open(file, 'rb') as pdf:
        reader = PdfReader(pdf)
        fields = reader.get_form_text_fields()
        if not fields or fields == {}:
            data = []
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    image = page.to_image(resolution=300)
                    text = pytesseract.image_to_string(image.original)


# for testing
repo_root = Path(__file__).parents[1]
pdf_path = repo_root.joinpath('docs/F201 - Purchase and Sale Agreement test.pdf')
extracted_text = extract_pdf_data(pdf_path)
print(extracted_text)