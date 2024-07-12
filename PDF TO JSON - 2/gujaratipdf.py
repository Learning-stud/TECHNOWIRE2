import pytesseract
from pdf2image import convert_from_path


pdf = "./2023-EROLLGEN-S06-56-DraftRoll-Revision1-GUJ-1-WI.pdf"


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the Poppler binaries
poppler_path = r'C:\Program Files\poppler-24.02.0\Library\bin'

def textToPdf(pdf, start_page, end_page, poppler_path):
    text = ""
    pages = convert_from_path(pdf, first_page=start_page, last_page=end_page, poppler_path=poppler_path)

    for page in pages:
        text += pytesseract.image_to_string(page, lang='guj')
    return text


pdf_text = textToPdf(pdf, start_page=3, end_page=5, poppler_path=poppler_path)

print(pdf_text)
