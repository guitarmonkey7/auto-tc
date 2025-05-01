import os
from PyPDF2 import PdfReader


def extract_pdf_data(file: str) -> dict[str, str]:
    text = ""
    with open(file, 'rb') as pdf:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text()
    return text


# for testing
extracted_text = extract_pdf_data("/home/elijah/Documents/ChandleyGreenRealEstate/F201 - Purchase and Sale Agreement.pdf")
print(extracted_text)