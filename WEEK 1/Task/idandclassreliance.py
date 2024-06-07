import requests
from bs4 import BeautifulSoup
import json

url = "https://guidestarindia.org/Summary.aspx?CCReg=5245"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all elements with tag name "span" and class name "CPBData"
elements = soup.find_all("div", class_="CPBData")

# Create a dictionary to store the data
data_dict = {}

# Iterate through the elements and extract data
for element in elements:
    # Extract text content from the element
    data = element.get_text(strip=True)

    # Get the ID of the element
    element_id = element.attrs.get("id")

    # If the ID exists, add the data to the dictionary with the ID as the key
    if element_id:
        data_dict[element_id] = data

# Save data to JSON file
with open("tagdata.json", "w") as json_file:
    json.dump(data_dict, json_file, indent=4)

print("Data extracted and saved to JSON file.")
