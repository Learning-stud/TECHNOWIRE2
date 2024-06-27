# import requests
# from bs4 import BeautifulSoup
# import json

# url = "https://guidestarindia.org/Summary.aspx?CCReg=5245"

# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")

# # Find all <td> elements with class "CTPDataContentCellNoPad"
# content_cells = soup.find_all("td", class_="ContentCell")

# # List to store extracted data
# data_list = []

# # Iterate through each <td> element with class "CTPDataContentCellNoPad"
# for content_cell in content_cells:
#     # Extract text content from the cell
#     data = content_cell.get_text(strip=True)

#     # Remove unwanted symbols and tags
#     data = data.replace("\n", "").replace("\u00a0", "").replace(":", "").strip()

#     # Append cleaned data to the list
#     if data:
#         data_list.append(data)

# # Save data to JSON file
# with open("data.json", "w") as json_file:
#     json.dump(data_list, json_file, indent=4)

# # print("Data extracted and saved to JSON file.")
# # import requests
# # from bs4 import BeautifulSoup
# # import json

# # url = "https://guidestarindia.org/Summary.aspx?CCReg=5245"

# # response = requests.get(url)
# # soup = BeautifulSoup(response.content, "html.parser")

# # # Find all <td> elements with class "CTPDataContentCellNoPad"
# # content_cells1 = soup.find_all("td", class_="CTPDataContentCellNoPad")

# # # Find all <td> elements with another class (replace "AnotherClass" with the actual class name)
# # content_cells2 = soup.find_all("td", class_="CPBData")

# # # List to store extracted data for the first class
# # data_list1 = []

# # # Iterate through each <td> element with class "CTPDataContentCellNoPad"
# # for content_cell in content_cells1:
# #     # Extract text content from the cell
# #     data = content_cell.get_text(strip=True)

# #     # Remove unwanted symbols and tags
# #     data = data.replace("\n", "").replace("\u00a0", "").replace(":", "").strip()

# #     # Append cleaned data to the list
# #     if data:
# #         data_list1.append(data)

# # # List to store extracted data for the second class
# # data_list2 = []

# # # Iterate through each <td> element with the second class
# # for content_cell in content_cells2:
# #     # Extract text content from the cell
# #     data = content_cell.get_text(strip=True)

# #     # Remove unwanted symbols and tags
# #     data = data.replace("\n", "").replace("\u00a0", "").replace(":", "").strip()

# #     # Append cleaned data to the list
# #     if data:
# #         data_list2.append(data)

# # # Create a dictionary with both sets of data
# # data_dict = {
# #     "class1_data": data_list1,
# #     "class2_data": data_list2
# # }

# # # Save data to JSON file
# # with open("data.json", "w") as json_file:
# #     json.dump(data_dict, json_file, indent=4)

# # print("Data extracted and saved to JSON file.")
# import requests
# from bs4 import BeautifulSoup
# import json

# url = "https://guidestarindia.org/Summary.aspx?CCReg=5245"

# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")

# # Find all <td> elements with class "CTPDataContentCellNoPad"
# content_cells = soup.find_all("td", class_="CTPDataContentCellNoPad")

# # Dictionary to store key-value pairs
# data_dict = {}

# # Iterate through each <td> element with class "CTPDataContentCellNoPad"
# for content_cell in content_cells:
#     # Extract text content from the cell
#     data = content_cell.get_text(strip=True)

#     # Split the text into key and value pairs
#     key_value_pairs = data.split(":")

#     # Ensure we have a key-value pair
#     if len(key_value_pairs) == 2:
#         key = key_value_pairs[0].strip()  # Extract key
#         value = key_value_pairs[1].strip()  # Extract value
#         data_dict[key] = value  # Add to dictionary

# # Save data to JSON file
# with open("data.json", "w") as json_file:
#     json.dump(data_dict, json_file, indent=4)

# print("Data extracted and saved to JSON file.")
import requests
from bs4 import BeautifulSoup
import json

url = "https://guidestarindia.org/Summary.aspx?CCReg=5245"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Classes to extract content from
classes_to_extract = ["CTPDataContentCellNoPad", "CPBData"]

# Dictionary to store extracted data
data_dict = {}

# Iterate through each class
for class_name in classes_to_extract:
    # Find all elements with the class
    elements = soup.find_all(["td", "tr", "span", "div"], class_='CTPDataContentCellNoPad')

    # List to store text content
    content_list = []

    # Iterate through each element and extract text content
    for element in elements:
        content = element.get_text(strip=True)
        if content:
            content_list.append(content)

    # Add content list to the dictionary with the class name as the key
    data_dict[class_name] = content_list

# Save data to JSON file
with open("data.json", "w") as json_file:
    json.dump(data_dict, json_file, indent=4)

print("Data extracted and saved to JSON file.")
