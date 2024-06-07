# import requests
# from bs4 import BeautifulSoup

# url = "https://guidestarindia.org/Summary.aspx?CCReg=5245"

# response = requests.get(url)

# soup = BeautifulSoup(response.content, "html.parser")
# # print(soup.get_text())

# content_cells = soup.find_all("td", class_="ContentCell")


# data_dict = {}

# for index, cell in enumerate(content_cells, start=1):
#     data = ""
#     nested_tags = cell.find_all(recursive=False)
#     for tag in nested_tags:
#         if tag.get_text().strip():
#             data += tag.get_text().strip()
#     data_dict[f"Data in <td class='ContentCell'> {index}"] = data.strip()

# # print(data_dict)

# for key, value in data_dict.items():
#     print(f"{key}: {value}")


# import requests
# from bs4 import BeautifulSoup

# url = "https://guidestarindia.org/Summary.aspx?CCReg=5245"

# response = requests.get(url)

# soup = BeautifulSoup(response.content, "html.parser")

# content_cells = soup.find_all("td", class_="ContentCell")

# data_dict = {}

# for index, cell in enumerate(content_cells, start=1):
#     data = ""
#     nested_tags = cell.find_all(recursive=False)
#     for tag in nested_tags:
#         if tag.get_text().strip():
#             data += tag.get_text().strip()
#     # Remove both spaces and newlines from the data
#     data_cleaned = ''.join(data.split())
#     # Create key-value pair
#     data_dict[index] = data_cleaned

# print(data_dict)

import requests
from bs4 import BeautifulSoup

url = "https://guidestarindia.org/Summary.aspx?CCReg=5245"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

content_cells = soup.find_all("td", class_="ContentCell")

data_dict = {}

for index, cell in enumerate(content_cells, start=1):
    data = ""
    nested_tags = cell.find_all(recursive=False)
    for tag in nested_tags:
        if tag.get_text().strip():
            data += tag.get_text().strip()
    # Remove both spaces and newlines from the data
    data_cleaned = ''.join(data.split())
    # Create key-value pair
    data_dict[index] = data_cleaned

# Print key-value pairs line by line
for key, value in data_dict.items():
    print(f"{key}: {value}")




# import requests
# from bs4 import BeautifulSoup
# import json

# # Define the URL
# url = "https://guidestarindia.org/Summary.aspx?CCReg=5245"

# # Send a GET request to the URL
# response = requests.get(url)

# # Parse the HTML content of the page
# soup = BeautifulSoup(response.content, "html.parser")

# # Find the <td> tag with class="ContentCell"
# content_cell = soup.find("td", class_="ContentCell")

# # Initialize a dictionary to store the extracted data
# data_dict = {}

# # Extract the organization name
# organization_name = content_cell.find("h3").get_text().strip()
# data_dict["Organization Name"] = organization_name

# # Extract other details
# details = content_cell.find("div", class_="address").get_text().strip().split("\n\n")
# for detail in details:
#     if detail:
#         key, value = detail.split("\n", 1)
#         data_dict[key.strip()] = value.strip()

# # Save the extracted data to a JSON file
# with open("extracted_data.json", "w") as json_file:
#     json.dump(data_dict, json_file, indent=4)

# print("Extracted data saved to extracted_data.json")
# import requests
# from bs4 import BeautifulSoup
# import json

# # Define the URL
# url = "https://guidestarindia.org/Summary.aspx?CCReg=5245"

# # Send a GET request to the URL
# response = requests.get(url)

# # Parse the HTML content of the page
# soup = BeautifulSoup(response.content, "html.parser")

# # Find the <td> tag with class="ContentCell"
# content_cell = soup.find("td", class_="ContentCell")

# # Initialize a dictionary to store the extracted data
# data_dict = {}

# # Extract the organization name
# organization_name = content_cell.find("h3").get_text().strip()
# data_dict["Organization Name"] = organization_name

# # Extract other details
# for div in content_cell.find_all("div"):
#     key = div.find("div").get_.strip()
#     value = div.find("span").get_text().strip()
#     data_dict[key] = value

# # Save the extracted data to a JSON file
# with open("extracted_data.json", "w") as json_file:
#     json.dump(data_dict, json_file, indent=4)

# print("Extracted data saved to extracted_data.json")