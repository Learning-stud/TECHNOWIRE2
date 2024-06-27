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
elements = soup.find_all(class_="CTPParaClippingHeaderLabel")

# Initialize dictionary to store data
data = {}

# Loop through each element
for element in elements:
    # Find all elements with class 'CPBData' within the current element
    cpb_data_elements = element.find_all(class_="CPBData")

    # Loop through each CPBData element
    for cpb_data in cpb_data_elements:
        # Extract key from the first span tag
        key = cpb_data.find('span').text.strip()

        # Extract values from the rest of the span tags
        values = [span.text.strip() for span in cpb_data.find_all('span')[1:]]

        # Add key-value pair to data dictionary
        data[key] = values

# Convert dictionary to JSON format
json_data = json.dumps(data, indent=4)

# Print the resulting JSON data
print(json_data)
