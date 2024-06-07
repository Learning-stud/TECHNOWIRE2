import requests
from bs4 import BeautifulSoup
import json

url = "https://guidestarindia.org/Summary.aspx?CCReg=5245"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all elements with class "CTPParaClippingHeaderLabel" (keys)
keys = soup.find_all(class_="CTPParaClippingHeaderLabel")

# Find all elements with class "CPBData" (values)
values = soup.find_all(class_="CPBData")

# Dictionary to store key-value pairs
data_dict = {}

# Ensure the number of keys and values are equal
num_keys = len(keys)
num_values = len(values)

# Iterate over keys and values and organize them into key-value pairs
for index in range(min(num_keys, num_values)):
    key = keys[index].get_text().strip()
    value = values[index].get_text().strip()
    data_dict[key] = value

# Save data to JSON file
with open("reliance5classname.json", "w") as json_file:
    json.dump(data_dict, json_file, indent=4)

print("Data extracted and saved to JSON file.")
