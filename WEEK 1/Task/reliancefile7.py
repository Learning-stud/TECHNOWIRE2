import requests
from bs4 import BeautifulSoup
import json

url = "https://guidestarindia.org/Summary.aspx?CCReg=5245"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all elements with class "CTPDataTable"
data_table_elements = soup.find_all(class_="CTPDataTable")

# Dictionary to store data associated with each "CTPDataTable"
data_dict = {}

# Loop through each "CTPDataTable" element
for index, table_element in enumerate(data_table_elements, start=1):
    # Find all table rows (tr elements)
    rows = table_element.find_all("tr")

    # Dictionary to store data for current table
    table_data = {}

    # Loop through each table row
    for row in rows:
        # Find all table header cells (th elements) and table data cells (td elements)
        headers = row.find_all("th")
        data_cells = row.find_all("td")

        # Extract text from headers and data cells and store as key-value pairs
        for header, data_cell in zip(headers, data_cells):
            key = header.get_text().strip()
            value = data_cell.get_text().strip()
            table_data[key] = value

    # Store data for current table in main dictionary
    data_dict[f"Table {index}"] = table_data

# Save data to JSON file
with open("data.json", "w") as json_file:
    json.dump(data_dict, json_file, indent=4)

print("Data extracted and saved to JSON file.")
