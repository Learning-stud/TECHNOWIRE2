import requests
from bs4 import BeautifulSoup
import json

# URL of the webpage
url = "https://guidestarindia.org/Organisation.aspx?CCReg=5348"

# GET request to the URL
response = requests.get(url)

# Parsing the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all elements with class 'CTPParaClippingHeaderLabelInline'
elements = soup.find_all(class_="CPBData")

# Initializing  dictionary to store data
data = {}

# Extract key-value pairs
for element in elements:
    span_tags = element.find_all('span')
    for i in range(len(span_tags)):
        if not span_tags[i].has_attr('class'):  # Check if the  span tag has no class
            key = span_tags[i].text.strip()
            value = span_tags[i-1].text.strip()
            # Remove unwanted symbols
            key = key.replace('\r\n', '').replace('\n', '').replace('\u00a0', '').strip()
            value = value.replace('\r\n', '').replace('\n', '').replace('\u00a0', '').strip()
            data[key] = value

# file name
file_name = "orgdata.json"

#  data to JSON file
with open(file_name, 'w') as json_file:
    json.dump(data, json_file, indent=2)

print(f"Data has been saved to {file_name}") 
