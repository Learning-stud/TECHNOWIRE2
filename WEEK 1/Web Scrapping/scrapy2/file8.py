# extracting image information in web page

import requests
from bs4 import BeautifulSoup

# Fetch the webpage containing the links
web = requests.get("http://books.toscrape.com/")
output = BeautifulSoup(web.content, "html.parser")

# Extract image from each link
img = output.find_all("img")
for images in img:
 print(images.get("src"))