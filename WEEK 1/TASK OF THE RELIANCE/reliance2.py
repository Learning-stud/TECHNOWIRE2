import requests
from bs4 import BeautifulSoup
import json


url = "https://guidestarindia.org/Summary.aspx?CCReg=5245"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# Example: Extracting data based on class name "ContentCell"
content_cells = soup.find_all("td", class_="ContentCell")

data_dict = {}

def process_text(text):
    lines = text.split("\n")  # Split text into lines
    clean_lines = [line.strip() for line in lines if line.strip()]  # Remove spaces and empty lines
    return " ".join(clean_lines)

for index, cell in enumerate(content_cells, start=1):
    data = ""
    nested_tags = cell.find_all(recursive=False)
    for tag in nested_tags:
        if tag.get_text().strip():
            data += tag.get_text().strip()
    data = process_text(data)
    data_dict[f"Data in <td class='ContentCell'> {index}"] = data.strip()

 # Extracting data based on ID "some_id"
some_id_element = soup.find(id="")
if some_id_element:
     data_dict["Data based on ID"] = some_id_element.get_text().strip()

with open("data.json", "w") as json_file:
    json.dump(data_dict, json_file, indent=4, separators=(',', ': '))  # Specify separators

print("Data extracted to JSON file.")
