import os
from pypdf import PdfReader
from pathlib import Path
import json


def extract_pdf_data(file: Path) -> dict[str, str] | str:
    with open(file, "rb") as pdf:
        reader = PdfReader(pdf)
        fields = reader.get_form_text_fields()
        if fields is None or fields == {}:
            pdf_text = ""
            total_pages = len(reader.pages)
            for i in range(total_pages):
                page = reader.pages[i]
                text = page.extract_text()
                pdf_text += text
            return pdf_text
        else:
            return fields


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


if __name__ == "__main__":
    # begin actual manual code Elijah added
    repo_root = Path(__file__).parents[1]
    pdf_path = repo_root.joinpath("docs/F201 - Purchase and Sale Agreement test.pdf")

    data = extract_pdf_data(pdf_path)
    json_output = json.dumps(data, indent=2)
    print("\n JSON Output:")
    print(json_output)

    save_location = os.path.join(os.path.expanduser("~"), "Documents")
    with open(os.path.join(save_location, "output.json"), "w") as f:
        f.write(json_output)
