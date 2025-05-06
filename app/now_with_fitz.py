import pymupdf as fitz
from pathlib import Path
import os

def get_fields(file):
    pdf = fitz.open(file)
    # print(pdf.metadata)

    # page = pdf[0]
    # # blocks = page.get_text("blocks", sort=True)
    # pgdict = page.get_text('dict', sort=True)
    # for block in pgdict['blocks']:
    #     if(block['type'] == 0):
    #         for line in block['lines']:
    #             for span in line['spans']:
    #                 print(span)

    page = pdf[0]
    words = page.get_text("words", sort=True)
    
    for i, word in enumerate(words):
        # information items will be found prefixed with their "key"
        text = word[4]
        if text == "Address:":  # the following word will be the date!
            address = words[i + 1][4]
            print("Property Address:", address) # This unfortunately still does not include the actual field value.
        # elif text == "Subtotal":
        #     subtotal = words[i + 1][4]
        #     print("Subtotal:", subtotal)
        # elif text == "Tax":
        #     tax = words[i + 1][4]
        #     print("Tax:", tax)
        # elif text == "INVOICE":
        #     inv_number = words[i + 2][4]  # skip the "#" sign
        #     print("Invoice number:", inv_number)
        # elif text == "BALANCE":
        #     balance = words[i + 2][4]  # skip the word "DUE"
        #     print("Balance due:", balance)
    


repo_root = Path(__file__).parents[1]
pdf_path = repo_root.joinpath('docs/F201 - Purchase and Sale Agreement test.pdf')
    
get_fields(pdf_path)
