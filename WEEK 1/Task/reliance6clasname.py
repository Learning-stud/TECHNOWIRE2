 # Class Name # CTPDataContentCell
import requests
from bs4 import BeautifulSoup
import json

url = "https://guidestarindia.org/Summary.aspx?CCReg=5245"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all elements with class "CTPDataContentCell"
data_elements = soup.find_all(class_="CTPDataContentCell")

# List to store data
data_list = []

# Loop through each element and extract its text content
for data_element in data_elements:
    data_text = data_element.get_text().strip()
    data_list.append(data_text)

# Save data to JSON file
with open("reliance7Classname.json", "w") as json_file:
    json.dump(data_list, json_file, indent=4)

print("Data extracted and saved to JSON file.")

