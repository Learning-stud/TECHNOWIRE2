
import requests
from bs4 import BeautifulSoup
import json


response = requests.get("https://www.flipkart.com/")
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

elements = soup.find_all(class_="uAl2uE")

text_list = [element.get_text(strip=True) for element in elements]

extracted_data = {"text": text_list}

json_data = json.dumps(extracted_data, indent=4)

print(json_data)



