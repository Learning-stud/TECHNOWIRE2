# import fitz  # PyMuPDF
# import pytesseract
# from PIL import Image
# import io
# import re
# import json

# # Define the path to the Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# def pdf_page_to_image(pdf_path, page_number):
#     # Open the PDF file
#     pdf_document = fitz.open(pdf_path)

#     # Select the page
#     page = pdf_document.load_page(page_number)

#     # Convert the page to an image
#     pix = page.get_pixmap()
#     img_data = pix.tobytes("ppm")
#     img = Image.open(io.BytesIO(img_data))

#     return img

# def extract_text_from_image(img):
#     # Use Tesseract to do OCR on the image
#     text = pytesseract.image_to_string(img)
#     return text

# def extract_key_value_pairs(text):
#     # Split the text into lines
#     lines = text.split('\n')

#     key_value_pairs = {}

#     # Define patterns to detect lines with key-value pairs
#     value_pattern = re.compile(r'Rs\. ([\d,]+)')

#     key = None

#     for line in lines:
#         # Check if the line contains 'Rs.' and capture the value
#         value_match = value_pattern.search(line)
#         if value_match and key:
#             value_str = value_match.group(1).replace(",", "")
#             try:
#                 value = float(value_str)
#             except ValueError:
#                 value = None
#             key_value_pairs[key] = value
#             key = None
#             continue

#         # If the line doesn't contain an amount, it is a key
#         if not value_match:
#             key = line.strip()

#     return key_value_pairs

# # Path to the PDF file
# pdf_path = './pages1-4.pdf'

# # Convert the first page to an image
# img = pdf_page_to_image(pdf_path, 0)

# # Extract text from the image
# text = extract_text_from_image(img)

# # Extract key-value pairs from the text
# key_value_pairs = extract_key_value_pairs(text)

# # Print the key-value pairs in JSON format
# print(json.dumps(key_value_pairs, indent=4))



# import PyPDF2
# import re

# def extract_names_and_amounts(pdf_path):
#     text = ""
#     with open(pdf_path, "rb") as file:
#         reader = PyPDF2.PdfReader(file)
#         first_page = reader.pages[0]
#         text = first_page.extract_text()

#     names = []
#     amounts = []

#     lines = text.split('\n')
#     start_index = None
#     end_index = None

#     # Find the start and end of the table based on keywords
#     for i, line in enumerate(lines):
#         if "PARTICULARS" in line.upper():
#             start_index = i
#         if "AMOUNT (IN RS.)" in line.upper():
#             end_index = i
#             break

#     if start_index is None or end_index is None:
#         raise ValueError("Table headers not found in the first page.")

#     # Extract names and amounts separately
#     for i in range(start_index + 1, end_index):
#         columns = lines[i].split(maxsplit=1)
#         if len(columns) >= 2:
#             names.append(columns[0].strip())
#             amounts.append(columns[1].strip())

#     # Combine names and amounts into a structured dictionary
#     data = {name: amount for name, amount in zip(names, amounts)}

#     return data

# # Path to your PDF file
# pdf_path = "./pdffile.pdf"

# try:
#     extracted_data = extract_names_and_amounts(pdf_path)
#     print("Extracted Data:")
#     for key, value in extracted_data.items():
#         print(f"{key}: {value}")
# except Exception as e:
#     print(f"Error: {e}")
import fitz  # PyMuPDF

# Open the PDF file
pdf_file = "./pages1-4.pdf"
doc = fitz.open(pdf_file)

# Iterate through each page
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text = page.get_text()
    print(f"Page {page_num + 1}:\n{text}\n")

# Close the PDF file
doc.close()
