import requests
from bs4 import BeautifulSoup

web = requests.get("http://books.toscrape.com/")
output = BeautifulSoup(web.content, "html.parser")

titles = output.find_all("a")
print(titles)