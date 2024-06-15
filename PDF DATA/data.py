import fitz
import pandas as pd

pdf_document = "PDFFILE.pdf"
doc = fitz.open(pdf_document)

data = []

for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text = page.get_text("text")
    data.append(text)

df = pd.DataFrame(data, columns=["Page_Content"])

df.to_csv("PDFFILE_extracted.csv", index=False)

print("Data extracted and saved to PDFFILE_extracted.csv")



