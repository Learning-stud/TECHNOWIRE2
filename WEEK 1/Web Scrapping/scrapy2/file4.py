# NAVIGABLE STRINGS
import requests
from bs4 import BeautifulSoup

web = requests.get("http://books.toscrape.com/")
output = BeautifulSoup(web.content, "html.parser")
# Navigable String
navigation = output.a.string
print(navigation)