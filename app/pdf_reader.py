import os
from pypdf import PdfReader
from pathlib import Path
import pdfplumber
import pytesseract
import json
from PIL import Image
import tempfile

# the commented out code "works" by printing out the full original document, and then 
# printing out all of the filled in fields at the bottom. It is almost useful except
# there is no way to get key-value pairs reliably without a lot of manual manupulation.

# def extract_pdf_data(file: str) -> dict[str, str] | list[str]:
#     with open(file, 'rb') as pdf:
#         reader = PdfReader(pdf)
#         fields = reader.get_form_text_fields()
#         if fields == None or fields == {}:
#             pdf_text = ''
#             total_pages = len(reader.pages)
#             for i in range(total_pages):
#                 page = reader.pages[i]
#                 text = page.extract_text()
#                 pdf_text += text
#             return pdf_text
#         else:
#             return fields


# # for testing
# repo_root = Path(__file__).parents[1]
# pdf_path = repo_root.joinpath('docs/F201 - Purchase and Sale Agreement test.pdf')
# extracted_text = extract_pdf_data(pdf_path)
# print(extracted_text)


#######################################################
# The rest of this was purely "vibe coded" and will be modified to be usable.
# The basic logic got us close but the splitting rules are primitive and assume that
# every colon in the document indicates a key:value pair, which is not accurate.
# Further splitting/stripping/sorting logic will need to be applied.


def extract_form_fields(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        fields = reader.get_form_text_fields()
        return fields if fields else {}
    except Exception as e:
        print("Form field extraction error:", e)
        return {}


def ocr_fallback(pdf_path):
    extracted_text = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                image = page.to_image(resolution=300).original
                temp_img_path = os.path.join(tempfile.gettempdir(), f"page_{i}.png")
                image.save(temp_img_path, "PNG")
                text = pytesseract.image_to_string(Image.open(temp_img_path))
                extracted_text.append(text)
                os.remove(temp_img_path)
    except Exception as e:
        print("OCR error:", e)
    return "\n".join(extracted_text)


def parse_key_value_pairs(text):
    kv_pairs = {}
    lines = text.splitlines()
    for line in lines:
        if ":" in line:
            parts = line.split(":", 1)
            key = parts[0].strip()
            value = parts[1].strip()
            if key and value:
                kv_pairs[key] = value
    return kv_pairs


def extract_pdf_data(pdf_path):
    print(f"🔍 Extracting data from: {pdf_path}")
    
    form_data = extract_form_fields(pdf_path)
    if form_data:
        print("✅ Extracted structured form fields.")
        return form_data

    print("⚠️ No form fields found. Falling back to OCR.")
    ocr_text = ocr_fallback(pdf_path)
    kv_data = parse_key_value_pairs(ocr_text)
    print("📝 Extracted data via OCR.")
    return kv_data


if __name__ == "__main__":
    # begin actual manual code Elijah added
    repo_root = Path(__file__).parents[1]
    pdf_path = repo_root.joinpath('docs/F201 - Purchase and Sale Agreement test.pdf')
    
    data = extract_pdf_data(pdf_path)
    json_output = json.dumps(data, indent=2)
    print("\n JSON Output:")
    print(json_output)

    save_location = os.path.join(os.path.expanduser("~"), "Documents")
    with open(os.path.join(save_location, "output.json"), "w") as f:
        f.write(json_output)