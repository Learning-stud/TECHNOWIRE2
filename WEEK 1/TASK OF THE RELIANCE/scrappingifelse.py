import requests
from bs4 import BeautifulSoup
import json

# URL of the webpage
url = "https://guidestarindia.org/Summary.aspx?CCReg=5348"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all elements with class 'CPBData'
elements = soup.find_all(class_="CPBData")

# Initialize list to store values
values = []

# Loop through each element
for element in elements:
    # Find all span tags within the current element
    span_tags = element.find_all('span')

    # Extract values from span tags
    for span in span_tags:
        # Exclude span tags that have class attribute
        if not span.has_attr('class'):
            values.append(span.text.strip())

# Convert list to JSON format
json_data = json.dumps(values, indent=4)

# Print the resulting JSON data
print(json_data)


#  this is running and giving the data but the values are repeating so in next trial i willl remove the values  which are repeating