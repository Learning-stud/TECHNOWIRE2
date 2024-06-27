# import fitz
# import pandas as pd

# pdf_document = "PDFFILE.pdf"
# doc = fitz.open(pdf_document)

# data = []

# for page_num in range(len(doc)):
#     page = doc.load_page(page_num)
#     text = page.get_text("text")
#     data.append(text)

# df = pd.DataFrame(data, columns=["Page_Content"])

# df.to_csv("PDFFILE_extracted.csv", index=False)

# print("Data extracted and saved to PDFFILE_extracted.csv")

import fitz
import pandas as pd
import os
import re
import json


def text_to_extract(path):
    data = []
    with fitz.open(path) as doc:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text("text")
            data.append(text)
    return data


def hindi_text(text):
    hindi_text_pattern = re.compile('[\u0900-\u097F]+')
    return hindi_text_pattern.sub('', text)


def  section_details(text, section):
    text = hindi_text(text)
    starting = text.find(section)
    if starting == -1:
        return {}

    ending = text.find("Details", starting + len(section))
    if ending == -1:
        ending = len(text)

    section_text = text[starting:ending].strip()
    words = section_text.split('\n')
    details = {}

    key = ""
    for texts in words:
        if ":" in texts:
            parts = texts.split(":", 1)
            key = parts[0].strip()
            value = parts[1].strip()
            details[key] = value
        elif key:
            details[key] += f" {texts.strip()}"

    return details


directory = os.getcwd()
print(f"Current Directory: {directory}")

# Define the PDF path
path = r'c:\Users\Jay\OneDrive\Documents\Desktop\TECHNOWIRE\PDF DATA\PDFFILE.pdf'
print(f"PDF Path: {path}")

# Ensure the file exists at the provided path
if not os.path.exists(path):
    raise FileNotFoundError(f"The file was not found at the specified path: {path}")

# Extract text from the PDF
list = text_to_extract(path)

# Combine the text from all pages
text = "\n".join(list)
text = hindi_text(text)

sections = [
    "Organisation Details",
    "Buyer Details",
    "Financial Approval Details",
    "Paying Authority Details",
    "Consignee Details"
]

all_details = {}
for section in sections:
    details =  section_details(text, section)
    all_details[section] = details

output = {}
for section, details in all_details.items():
    output[section] = details

print(json.dumps(output, indent=4))


