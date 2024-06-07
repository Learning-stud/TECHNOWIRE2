import requests
from bs4 import BeautifulSoup

web = requests.get("https://books.toscrape.com/")
web.status_code
web.content

# for getting the out into proper html format e=we have use pretiffy
# by passing html parser we give the interpreter the permission to print it into html format

output = BeautifulSoup(web.content,"html.parser")
# print(output.prettify())

print(output.title)