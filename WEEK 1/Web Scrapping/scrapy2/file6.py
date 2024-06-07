# finding elements in web page  scrapping

# finding elements by id and another is by class


import requests
from bs4 import BeautifulSoup

# Fetch the webpage containing the links
web = requests.get("http://books.toscrape.com/")
output = BeautifulSoup(web.content, "html.parser")

# Find all the links (<a> tags) on the webpage
links = output.find_all("a")

# Extract text from each link
for link in links:
    link_text = link.text
    print("Text:", link_text)


 # extracting data from link to another link and after that converting all {p , a , h1 and other } text those containing text and converting them into text  