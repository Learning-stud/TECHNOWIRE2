import requests
from bs4 import BeautifulSoup
import json


url = "https://guidestarindia.org/Summary.aspx?CCReg=5245"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# Find all elements with the class name "CTPDataContentCellNoPad"
data_elements = soup.find_all(class_="CTPParaClippingHeaderLabel")

data_dict = {}

def process_text(text):
    lines = text.split("\n")  # Split text into lines
    clean_lines = [line.strip() for line in lines if line.strip()]  # Remove spaces and empty lines
    return " ".join(clean_lines)

for index, element in enumerate(data_elements, start=1):
    data = process_text(element.get_text())
    data_dict[f"Data {index}"] = data.strip()

with open("dataclass4.json", "w") as json_file:
    json.dump(data_dict, json_file, indent=4, separators=(',', ': '))  # Specify separators

print("Data extracted to JSON file.")
