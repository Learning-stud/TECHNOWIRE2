# CPBData
import requests
from bs4 import BeautifulSoup
import json

# URL of the webpage
url = "https://guidestarindia.org/Summary.aspx?CCReg=5348"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all elements with class 'CTPParaClippingHeaderLabel'
elements = soup.find_all(class_="CPBData")

# Initialize dictionary to store data
data = {}

# Extract key-value pairss
for element in elements:
    span_tags = element.find_all('span')
    for i in range(len(span_tags)):
        if not span_tags[i].has_attr('class'):  # Check if span tag has no class
            key = span_tags[i].text.strip()
            value = span_tags[i-1].text.strip()
            data[key] = value

# Define file name
file_name = "summerydata.json"

# Write data to JSON file
with open(file_name, 'w') as json_file:
    json.dump(data, json_file, indent=2)

print(f"Data has been saved to {file_name}")
