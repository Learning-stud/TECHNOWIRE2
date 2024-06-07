import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://guidestarindia.org/Search.aspx?q=+reliance"
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all elements with the class name "CPBData"
    cpb_data_elements = soup.find_all(class_="CPBData")

    # Loop through each CPBData element
print(cpb_data_elements)