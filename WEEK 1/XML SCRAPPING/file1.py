import requests
from lxml import etree

# Fetch the HTML content of a webpage
url = "https://www.investing.com/holiday-calendar/"
response = requests.get(url)
html_content = response.text

# Parse the HTML
html_tree = etree.HTML(html_content)

# Example XPath expression: select all links (anchor tags)
links = html_tree.xpath("//a/@href")

# Print the links
for link in links:
    print(link)
