from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed. You can use other browsers as well.

# Navigate to the website
url = "https://guidestarindia.org/Summary.aspx?CCReg=5348"
driver.get(url)

# Find all elements with class "CPBData"
cpb_data = driver.find_elements(By.CLASS_NAME, "CPBData")

# Initialize an empty dictionary to store key-value pairs
data_dict = {}

# Iterate through each element
for element in cpb_data:
    # Find all <span> and <a> tags within the element
    spans = element.find_elements(By.TAG_NAME, "span")
    links = element.find_elements(By.TAG_NAME, "a")

    # Extract text from <span> tags and store in dictionary
    for span in spans:
        key = span.get_attribute("id")  # Assuming id attribute as key
        value = span.text.strip()
        data_dict[key] = value

    # Extract href attribute from <a> tags and store in dictionary
    for link in links:
        key = link.get_attribute("id")  # Assuming id attribute as key
        value = link.get_attribute("href")
        data_dict[key] = value

# Print the extracted key-value pairs
for key, value in data_dict.items():
    print(key + ":", value)

# Close the WebDriver
driver.quit()
