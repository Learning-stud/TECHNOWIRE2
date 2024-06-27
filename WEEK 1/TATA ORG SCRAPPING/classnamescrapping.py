

# # # ====================================================================================================================================================
# import requests
# from bs4 import BeautifulSoup

# # Send a GET request to the website
# url = "https://guidestarindia.org/Summary.aspx?CCReg=5348"
# response = requests.get(url)

# # Parse the HTML content
# soup = BeautifulSoup(response.text, "html.parser")

# # Find all <div> elements with class "CPBData"
# div_elements = soup.find_all("div", class_="CPBData")

# # Initialize an index for keys
# index = 1

# # Iterate through <div> elements and extract text from <span> and <a> tags
# for div in div_elements:

#     # Find all <span> and <a> tags within the <div> element
#     spans = div.find_all("span")
#     links = div.find_all("a")

#     # Print text from <span> tags
#     for span in spans:
#         text = span.get_text(strip=True)
#         text = text.replace(" ", "")  # Remove spaces
#         print( text)
import requests
from bs4 import BeautifulSoup
import json

# URL of the webpage
url = "https://guidestarindia.org/Summary.aspx?CCReg=5348"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all elements with class 'CPBData'
    elements = soup.find_all(class_="CPBData")

    # Initialize dictionary to store data
    data = {}

    # Extract key-value pairs
    for element in elements:
        span_tags = element.find_all('span')
        anchor_tags = element.find_all('a')
        for i in range(len(span_tags)):
            # Extract text from span tag
            key = span_tags[i].text.strip()
            if i < len(anchor_tags) and not anchor_tags[i].has_attr('class'):
                # Extract URL from anchor tag
                value = anchor_tags[i]['href']
            else:
                value = span_tags[i-1].text.strip()
            # Remove unwanted symbols
            key = key.replace('\r\n', '').replace('\n', '').replace('\u00a0', '').strip()
            value = value.replace('\r\n', '').replace('\n', '').replace('\u00a0', '').strip()
            data[key] = value

    file_name = "summerydata.json"

    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=2)

    print(f"Data has been saved to {file_name}")
else:
    print("Failed to retrieve webpage.")