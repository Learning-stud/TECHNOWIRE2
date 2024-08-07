import fitz
import json

pdf_file = "./2023-EROLLGEN-S06-56-DraftRoll-Revision1-GUJ-1-WI.pdf"

doc = fitz.open(pdf_file)

data = {}

for page_num in range(2, 8):
    page = doc.load_page(page_num) 
    text = page.get_text()

    clean_text = text.replace('\n', ' ')

    data[f"Page {page_num + 1}"] = clean_text

doc.close()

with open("results.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Data has been successfully extracted and saved to financial_results.json.")
