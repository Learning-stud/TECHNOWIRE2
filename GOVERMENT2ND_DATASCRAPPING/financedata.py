import requests
from bs4 import BeautifulSoup
import json

url = "https://guidestarindia.org/Finances.aspx?CCReg=5348"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(class_="CPBData")
    data = {}

    for element in elements:
        span = element.find_all('span')
        anchor_tags = element.find_all('a')


        for i in range(len(span)):
            key = span[i].text.strip()

            if i < len(anchor_tags) and not anchor_tags[i].has_attr('class'):
                value = anchor_tags[i]['href']
            else:# to remove unwanted text
                value = span[i-1].text.strip()
            key = key.replace('\r\n', '').replace('\n', '').replace('\u00a0', '').strip()
            value = value.replace('\r\n', '').replace('\n', '').replace('\u00a0', '').strip()
            data[key] = value

    file_name = "financedata.json"

    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=2)

    print(f"Data has been saved to {file_name}")
else:
    print("Failed to retrieve webpage.")
