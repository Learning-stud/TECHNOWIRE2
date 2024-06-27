# from lxml import html
# import requests

# url ="https://www.flipkart.com/search?q=apple&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

# responses= requests.get(url)

# html = responses.content

# tree = html.fromstring(responses.content)

# link_titles = tree.xpath('//a/text()')

# for title in link_titles:
#  print(title)


import requests
from lxml import html

url = "https://www.flipkart.com/search?q=apple&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
response = requests.get(url)
html_content = response.content.decode('utf-8')  # Decode the content to a string

tree = html.fromstring(html_content)
link_title = tree.xpath('//a/text()')

for title in link_title:
 print(title)
