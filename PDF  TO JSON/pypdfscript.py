# import json
# from PyPDF2 import PdfReader
# import re

# def extract_text_from_pdf(pdf_path):
#     pdf_text = []
#     reader = PdfReader(pdf_path)
#     for page in reader.pages:
#         pdf_text.append(page.extract_text())
#     return pdf_text

# def parse_financial_data(lines):
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

# def create_json_structure(pdf_text):
#     data = {}
#     for i, text in enumerate(pdf_text):
#         page_key = f"page_{i + 1}"
#         lines = text.split('\n')
#         page_data = parse_financial_data(lines)
#         data[page_key] = page_data
#     return data

# def save_to_json(data, output_path):
#     with open(output_path, 'w') as json_file:
#         json.dump(data, json_file, indent=4)

# # Path to the PDF file
# pdf_path = './pdffile.pdf'
# # Output path for the JSON file
# output_path = 'output.json'

# # Extract text from the PDF
# pdf_text = extract_text_from_pdf(pdf_path)
# # Create a JSON structure from the extracted text
# data = create_json_structure(pdf_text)
# # Save the JSON structure to a file
# save_to_json(data, output_path)

# print("Data has been extracted and saved to JSON file successfully.")




