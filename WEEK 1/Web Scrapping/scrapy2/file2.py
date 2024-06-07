import requests
from bs4 import BeautifulSoup

# Fetching webpage and parsing HTML
web = requests.get("https://books.toscrape.com/")
# For getting the content and then changing it to the HTML format
output = BeautifulSoup(web.content, "html.parser")
# For finding all paragraph tags
all_tags = output.find_all('a')
# Extracting data
for paragraph in all_tags:
    print(paragraph.text)
 