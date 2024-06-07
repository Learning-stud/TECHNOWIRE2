import requests
from bs4 import BeautifulSoup

web = requests.get("http://books.toscrape.com/")
output = BeautifulSoup(web.content, "html.parser")
all_tags = output.find_all()
for tag in all_tags:
    print(tag)
