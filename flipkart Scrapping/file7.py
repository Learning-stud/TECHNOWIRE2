# # # extracting link in web page

# # import requests
# # from bs4 import BeautifulSoup

# # # Fetch the webpage containing the links
# # web = requests.get("http://books.toscrape.com/")
# # output = BeautifulSoup(web.content, "html.parser")

# # # Extract text from each link
# # for l in output.find_all(""):
# #     print(l.get("href"))

# import requests
# from lxml import html
# import json

# # Fetch the webpage containing the links
# web = requests.get("http://books.toscrape.com/")
# output = html.fromstring(web.content)

# # Define the XPath expression to select all links
# xpath_expression = "//a/@href"

# # Extract links using XPath
# links = output.xpath(xpath_expression)[:5]  # Limit to 5 links

# # Create a list to store the extracted data
# extracted_data = []

# # Extracted data will be a list of dictionaries with a single key "url"
# for link in links:
#     extracted_data.append({"url": link})

# # Convert the extracted data to JSON format
# json_data = json.dumps(extracted_data, indent=4)

# # Write the JSON data to a file
# with open("data.json", "w") as json_file:
#     json_file.write(json_data)

# import requests
# from bs4 import BeautifulSoup
# import json

# # Fetch the webpage
# url = "https://www.flipkart.com/"
# response = requests.get(url)
# html_content = response.text

# # Parse the HTML
# soup = BeautifulSoup(html_content, "html.parser")

# # Find all <object> tags
# object_tags = soup.find_all("object")

# # Extract text from <a> tags within <object> tags
# link_names = []

# for object_tag in object_tags:
#     # Find all <a> tags within the current <object> tag
#     a_tags = object_tag.find_all("a")

#     # Extract text from <a> tags and append to link_names
#     for a_tag in a_tags:
#         link_names.append(a_tag.get_text(strip=True))

# # Create a list to store the extracted data
# extracted_data = {"link_names": link_names}

# # Convert the extracted data to JSON format
# json_data = json.dumps(extracted_data, indent=4)

# # Write the JSON data to a file or print it
# print(json_data)

# import requests
# from bs4 import BeautifulSoup
# import json

# # Fetch the webpage
# url = "https://www.flipkart.com/"
# response = requests.get(url)
# html_content = response.text

# # Parse the HTML
# soup = BeautifulSoup(html_content, "html.parser")

# # Find all elements with the class name "_1BJVlg"
# elements = soup.find_all(class_="_1BJVlg")

# # Extract names from elements
# names = []

# for element in elements:
#     # Extract the text from the element
#     name = element.get_text(strip=True)

#     # Append the name to the names list
#     names.append(name)

# # Create a dictionary to store the extracted data
# extracted_data = {"names": names}

# # Convert the extracted data to JSON format
# json_data = json.dumps(extracted_data, indent=4)

# # Write the JSON data to a file or print it
# print(json_data)
# import requests
# from bs4 import BeautifulSoup
# import json

# # Fetch the webpage
# url = "https://www.flipkart.com/"
# response = requests.get(url)
# html_content = response.text

# # Parse the HTML
# soup = BeautifulSoup(html_content, "html.parser")

# # Find all <div> tags with class "_16rZTH"
# div_elements = soup.find_all("div", class_="_16rZTH")

# # Extract text from <a> tags within <object> tags inside <div> elements
# link_names = []

# for div_element in div_elements:
#     # Find all <object> tags within the current <div> element
#     object_tags = div_element.find_all("object")

#     # Extract text from <a> tags within <object> tags
#     for object_tag in object_tags:
#         a_tags = object_tag.find_all("a")
#         for a_tag in a_tags:
#             link_names.append(a_tag.get_text(strip=True))

# # Create a dictionary to store the extracted data
# extracted_data = {"link_names": link_names}

# # Convert the extracted data to JSON format
# json_data = json.dumps(extracted_data, indent=4)

# # Write the JSON data to a file or print it
# print(json_data)
import requests
from bs4 import BeautifulSoup
import json

# Fetch the webpage

response = requests.get("https://www.flipkart.com/")
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find all elements with the class name "_3490ry"
elements = soup.find_all(class_="uAl2uE")

# Extract text from elements
text_list = [element.get_text(strip=True) for element in elements]

# Create a dictionary to store the extracted data
extracted_data = {"text": text_list}

# Convert the extracted data to JSON format
json_data = json.dumps(extracted_data, indent=4)

# Write the JSON data to a file or print it
print(json_data)



#  nott getting data just getting empty list
