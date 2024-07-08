# import json
# from PyPDF2 import PdfReader
# import re

# def text_to_pdf(pdf_path):
#     pdf_text = []
#     reader = PdfReader(pdf_path)
#     for page in reader.pages:
#         pdf_text.append(page.extract_text())
#     return pdf_text

# def adding_financial(lines):
#     financial_data = {}
#     current_section = None

#     for line in lines:
#         if re.match(r'^[A-Z\s&]+$', line):  # Detect section headers
#             current_section = line.strip().lower().replace(" ", "_").replace(".", "_").replace(":", "_")
#             financial_data[current_section] = {}
#         elif current_section:
#             match = re.match(r'^(.*?):\s*([\d,\.]+)$', line)
#             if match:
#                 key, value = match.groups()
#                 financial_data[current_section][key.strip()] = value.strip()
#             else:
#                 parts = line.split()
#                 if len(parts) > 1 and re.match(r'^[\d,\.]+$', parts[-1]):
#                     key = " ".join(parts[:-1])
#                     value = parts[-1]
#                     financial_data[current_section][key.strip()] = value.strip()
#                 else:
#                     financial_data[current_section][line.strip()] = ""

#     return financial_data

# def json_structure(pdf_text):
#     data = {}
#     for i, text in enumerate(pdf_text):
#         page_key = f"page_{i + 1}"
#         lines = text.split('\n')
#         page_data = adding_financial(lines)
#         data[page_key] = page_data
#     return data

# def saved_json(data, outputData):
#     with open(outputData, 'w') as json_file:
#         json.dump(data, json_file, indent=8)

# pdf_path = './Audited Financials - FY 24.pdf'
# outputData = 'data.json'

# pdf_text = text_to_pdf(pdf_path)
# data = json_structure(pdf_text)
# saved_json(data, outputData)

# print("Data has been extracted and saved to JSON file successfully.")
import PyPDF2
import re

# Function to extract all text from the PDF
def extract_all_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text() + "\n"
    return text

# Function to extract data based on provided headings
def extract_data_by_headings(text, headings):
    data = {heading: {} for heading in headings}
    current_heading = None

    # Split text into lines
    lines = text.split('\n')

    # Iterate over each line to organize data under the correct heading
    for line in lines:
        # Check if the line contains any of the headings
        for heading in headings:
            if heading in line:
                current_heading = heading
                break

        # If the line is under a heading, extract key-value pairs
        if current_heading:
            # Pattern to match amounts in rupees
            amount_pattern = re.compile(r"₹?\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?")
            if amount_pattern.search(line):
                amount_match = amount_pattern.search(line)
                amount = amount_match.group()
                key = line[:amount_match.start()].strip()
                key = ' '.join(key.split())
                if key and amount:
                    data[current_heading][key] = amount

    return data

# Path to the PDF file
pdf_path = "./Audited Financials - FY 24.pdf"

# Extract all text from the PDF
full_text = extract_all_text_from_pdf(pdf_path)

# Provided headings
headings = [

]

# Extract data based on provided headings
extracted_data = extract_data_by_headings(full_text, headings)

# Print the organized data
for heading, pairs in extracted_data.items():
    print(f"{heading}:")
    for key, value in pairs.items():
        print(f"  {key}: {value}")

































