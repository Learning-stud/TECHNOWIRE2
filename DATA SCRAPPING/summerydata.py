# CPBData
# url = "https://guidestarindia.org/Summary.aspx?CCReg=5348"
import requests
from bs4 import BeautifulSoup
import json

# -===========================/===================================/========================================/===============================================/

url = "https://guidestarindia.org/Summary.aspx?CCReg=5348"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

# -===========================/===================================/========================================/===============================================/


elements = soup.find_all(class_="CPBData")              #/====/ GETTING THE VALUES SITUATED IN THE CLASS NAME /=====/

# -===========================/===================================/========================================/===============================================/

data = {}
# a_data={}

# -===========================/===================================/========================================/===============================================/
                                               # /=======================/ FOR EXTRACTING THE DATA USING [ FOR IN ] /=========================/
for element in elements:
    span_tags = element.find_all('span')
    for i in range(len(span_tags)):                         # 
        if not span_tags[i].has_attr('class'):  # IF NO CLASS

                                                            # /========/ FOR GETTING THE VALUES IN KEY VALUE PAIR /=========/
            key = span_tags[i].text.strip()                 # KEY
            value = span_tags[i-1].text.strip()             # VALUE
            data[key] = value                               # STORED DATA

file_name = "summerydata.json"


# -===========================/===================================/========================================/===============================================/
                                                         # /========/ # GETTING ALL ANCHOR TAG DATA  /=========/

                                                                # for a_elements in elements:
                                                                #     a_tags = a_elements.find_all('a')
                                                                #     for a in range(len(a_tags)):
                                                                #         if not  a_tags:[a].has_attr("class"):
                                                                #         key = a_tags[a].text.strip()
                                                                #         value = a_tags[a-1].text.strip()
                                                                #         a_data[key] = value



# -===========================/===================================/========================================/===============================================/
                                            # /=======================/ SAVING INTO JSON FILE /=========================/
with open(file_name, 'w') as json_file:             # OPENING
    json.dump(data, json_file, indent=2)            # DUMPING DATA # INDENTATION OF 2

print(f"Data has been saved to {file_name}")
