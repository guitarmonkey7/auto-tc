import os
import json
from pypdf import PdfReader
from pathlib import Path


def extract_pdf_data(file: str):
    text = ""
    with open(file, 'rb') as pdf:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text()
    return text
        

if __name__ == "__main__":
    # begin actual manual code Elijah added
    repo_root = Path(__file__).parents[1]
    pdf_path = repo_root.joinpath('docs/F201 - Purchase and Sale Agreement test.pdf')
    
    data = extract_pdf_data(pdf_path)
    print(data)

    # save_location = os.path.join(os.path.expanduser("~"), "Documents")
    # with open(os.path.join(save_location, "output.json"), "w") as f:
    #     f.write(json_output)