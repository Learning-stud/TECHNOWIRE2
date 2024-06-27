# web scrapping is and process of getting any dat from website in an html or json format
# It is used for get any type of data ;
# while Using Scrapping you can get the data of any type there are two types od data form in web scrapping structured  format and unstructructed format

#  In structured format you get data in table or excel format
#  In unstructured type you will get data in video audio or images format.
import requests
web = requests.get("https://www.tutorialsfreak.com/")
print(web)
web.content
