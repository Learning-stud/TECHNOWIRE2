import requests
from bs4 import BeautifulSoup
import json

url = "https://guidestarindia.org/Summary.aspx?CCReg=5245"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all <td> elements with class "ContentCell"
content_cells = soup.find_all("td", class_="ContentCell")

# Dictionary to store data
data_dict = {}

# Iterate through each <td> element
for index, cell in enumerate(content_cells, start=1):
    # Find the inner table inside the <td> element
    inner_table = cell.find("table")

    if inner_table:
        # Extract data from the inner table
        table_data = []
        rows = inner_table.find_all("tr")
        for row in rows:
            # Remove special characters and empty strings from cell text
            row_data = [cell.get_text().strip().replace("\n", "").replace("\u00a0", "").strip() for cell in row.find_all("td")]
            # Filter out empty strings
            row_data = [data for data in row_data if data]
            table_data.append(row_data)

        # Store the table data in the dictionary
        data_dict[f"Table {index}"] = table_data

# Save data to JSON file
with open("reliancedata8classname.json", "w") as json_file:
    json.dump(data_dict, json_file, indent=4)

print("Data extracted and saved to JSON file.")


# ContentCell