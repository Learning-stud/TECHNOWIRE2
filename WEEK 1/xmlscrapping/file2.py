#  # using xpath doing web scrapping and then convert it into json file

# import requests
# from  lxml import etree
# import json


#  #  fetch the html content of a web page

# url = "https://www.investing.com/holiday-calendar/"
# response = requests.get(url)
# html_content= response.text


# #  parsing to html
# html_tree =  etree.HTML(html_content)

# #  selecting all links
# links = html_tree.xpath("//a")

# #  saving extracted data list
# data_extracted = []

# # dat_count=0

# for link in links:
#     link_data ={
#      'text':link.text,
#      'url':link.get('href')
#     }
#     data_extracted.append(link_data)

#  #  converting extracted data to json format
# # ========================================================================================================================
# json_data = json.dumps(data_extracted, indent=2)
# print(json_data)

# import requests
# from lxml import etree
# import json

# # Fetch the HTML content of a webpage
# url = "https://www.investing.com/holiday-calendar/"
# response = requests.get(url)
# html_content = response.text

# # Parse the HTML
# html_tree = etree.HTML(html_content)

# # Example XPath expression: select all links (anchor tags)
# links = html_tree.xpath("//a")

# # Create a list to store the extracted data
# extracted_data = []

# # Counter to track the number of data points extracted
# data_count = 0

# # Extract relevant information from each link
# for link in links:
#     link_data = {
#         "text": link.text,
#         "url": link.get("href")
#     }
#     extracted_data.append(link_data)
#     data_count += 1

#     # Check if the desired number of data points has been reached
#     if data_count >= 100:
#         break

# # Convert the extracted data to JSON format
# json_data = json.dumps(extracted_data, indent=4)

# # Print or save the JSON data
# print(json_data)


import requests
from lxml import etree
import json

# url = "https://www.investing.com/holiday-calendar/"
url = "https://www.flipkart.com/"
url = "https://www.flipkart.com/search?q=apple&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
response = requests.get(url)
html_content = response.text

# Parse the HTML
html_tree = etree.HTML(html_content)

# Example XPath expression: select all links (anchor tags)
links = html_tree.xpath("//a")

# Create a list to store the extracted data
extracted_data = []

# Counter to track the number of data points extracted
data_count = 0

# Extract relevant information from each link
for link in links:
    link_data = {
        "text": link.text,
        "url": link.get("href")
    }
    extracted_data.append(link_data)
    data_count += 1

    # Check if the desired number of data points has been reached
    if data_count >= 100:
        break

# Convert the extracted data to JSON format
json_data = json.dumps(extracted_data, indent=4)

# Print or save the JSON data
print(json_data)
