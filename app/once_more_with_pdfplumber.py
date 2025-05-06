import pdfplumber
import re
from pathlib import Path
from pdfplumber.utils.pdfinternals import resolve_and_decode, resolve

def parse_field_helper(form_data, field, prefix=None):
    """ appends any PDF AcroForm field/value pairs in `field` to provided `form_data` list

        if `field` has child fields, those will be parsed recursively.
    """
    resolved_field = field.resolve()
    field_name = '.'.join(filter(lambda x: x, [prefix, resolve_and_decode(resolved_field.get("T"))]))
    if "Kids" in resolved_field:
        for kid_field in resolved_field["Kids"]:
            parse_field_helper(form_data, kid_field, prefix=field_name)
    if "T" in resolved_field or "TU" in resolved_field:
        # "T" is a field-name, but it's sometimes absent.
        # "TU" is the "alternate field name" and is often more human-readable
        # your PDF may have one, the other, or both.
        alternate_field_name  = resolve_and_decode(resolved_field.get("TU")) if resolved_field.get("TU") else None
        field_value = resolve_and_decode(resolved_field["V"]) if 'V' in resolved_field else None
        form_data.append([field_name, alternate_field_name, field_value])


repo_root = Path(__file__).parents[1]
pdf_path = repo_root.joinpath('docs/F201 - Purchase and Sale Agreement test.pdf')
    
pdf = pdfplumber.open(pdf_path)

form_data = []
labels = pdf.lines
# fields = resolve(resolve(pdf.doc.catalog["AcroForm"])["Fields"])
# for field in fields:
#     parse_field_helper(form_data, field)

print(labels)