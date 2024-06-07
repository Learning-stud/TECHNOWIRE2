# # # from selenium import webdriver
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # from selenium.webdriver.support import expected_conditions as EC
# # # from bs4 import BeautifulSoup
# # # import time

# # # # Initialize WebDriver
# # # driver = webdriver.Chrome()

# # # # Define the URL
# # # url = "https://www.icra.in/Rating/RatingCategory?RatingType=CR&RatingCategoryId=5"
# # # driver.get(url)

# # # # Function to extract data from the current page
# # # def extract_data():
# # #     soup = BeautifulSoup(driver.page_source, 'html.parser')
# # #     table = soup.find('table', {'id': 'entity_data_table'})
# # #     rows = table.find_all('tr')
# # #     data = []
# # #     for row in rows:
# # #         cells = row.find_all('td')
# # #         data.append([cell.text.strip() for cell in cells])
# # #     return data

# # # # List to store all data
# # # all_data = []

# # # # Loop through pages and extract data
# # # for page in range(1, 5):  # Adjust the range according to the total number of pages
# # #     print(f"Scraping page {page}")
# # #     all_data.extend(extract_data())
# # #     try:
# # #         # Find and click the 'Next' button using XPath or a more reliable selector
# # #         next_button = WebDriverWait(driver, 10).until(
# # #             EC.element_to_be_clickable((By.XPATH, '//a'))
# # #         )
# # #         next_button.click()
# # #         time.sleep(20)  # Adjust sleep time if necessary
# # #     except Exception as e:
# # #         print(f"Failed to navigate to the next page: {e}")
# # #         break

# # # # Close the WebDriver
# # # driver.quit()

# # # # Print the data
# # # for row in all_data:
# # #     print(row)





# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from bs4 import BeautifulSoup
# # import time

# # # Initialize WebDriver
# # driver = webdriver.Chrome()

# # # Define the URL
# # url = "https://www.icra.in/Rating/RatingCategory?RatingType=CR&RatingCategoryId=5"
# # driver.get(url)

# # # Function to extract data from the current page
# # def extract_data():
# #     soup = BeautifulSoup(driver.page_source, 'html.parser')
# #     table = soup.find('table', {'id': 'entity_data_table'})
# #     rows = table.find_all('tr')
# #     data = []
# #     for row in rows:
# #         cells = row.find_all('td')
# #         data.append([cell.text.strip() for cell in cells])
# #     return data

# # # List to store all data
# # all_data = []

# # # Loop through pages and extract data
# # for page in range(1, 3):  # Adjust the range according to the total number of pages
# #     print(f"Scraping page {page}")
# #     all_data.extend(extract_data())
# #     try:
# #         # Find and click the 'Next' button using the correct XPath
# #         next_button = WebDriverWait(driver, 10).until(
# #             EC.element_to_be_clickable((By.XPATH, '//a'))
# #         )
# #         print("Next button found, clicking...")
# #         next_button.click()
# #         time.sleep(2)  # Adjust sleep time if necessary
# #     except Exception as e:
# #         print(f"Failed to navigate to the next page: {e}")
# #         break

# # # Close the WebDriver
# # driver.quit()

# # # Print the data
# # for row in all_data:
# #     print(row)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import time

# # Initialize WebDriver
# driver = webdriver.Chrome()

# # Define the URL
# url = "https://www.icra.in/Rating/RatingCategory?RatingType=CR&RatingCategoryId=5"
# driver.get(url)

# # Function to extract data from the current page
# def extract_data():
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     table = soup.find('table', {'id': 'entity_data_table'})
#     rows = table.find_all('tr')
#     data = []
#     for row in rows:
#         cells = row.find_all('td')
#         data.append([cell.text.strip() for cell in cells])
#     return data

# # List to store all data
# all_data = []

# # Loop through pages and extract data
# for page in range(1, 10):  # Adjust the range according to the total number of pages
#     print(f"Scraping page {page}")
#     all_data.extend(extract_data())
#     try:
#         # Find and click the 'Next' button using the correct XPath
#         next_button = WebDriverWait(driver, 200).until(
#             EC.element_to_be_clickable((By.XPATH, '//li[@class="PagedList-skipToNext"]/a'))

#         )
#         print("Next button found, clicking...")
#         next_button.click()
#         time.sleep(50)  # Adjust sleep time if necessary
#     except Exception as e:
#         print(f"Failed to navigate to the next page: {e}")
#         break

# # Close the WebDriver
# driver.quit()

# # Print the data
# for row in all_data:
#     print(row)





from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Define the URL
url = "https://www.icra.in/Rating/RatingCategory?RatingType=CR&RatingCategoryId=5"
driver.get(url)

# Function to extract data from the current page
def extract_data():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find('table', {'id': 'entity_data_table'})
    rows = table.find_all('tr')
    data = []
    for row in rows[1:]:  # Skip the header row
        cells = row.find_all('td')
        data.append([cell.text.strip() for cell in cells])
    return data

# List to store all data
all_data = []

# Loop to navigate through pages and extract data
page = 1
while True:
    print(f"Scraping page {page}")
    all_data.extend(extract_data())
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="contentPager"]/div/ul/li[5]/a')))
    if "k-state-disabled" in next_button.get_attribute("class"):
        print("Reached last page.")
        break
    next_button.click()
    time.sleep(5)  # Wait for page to load
    page += 1

# Close the WebDriver
driver.quit()

# Print the data
for row in all_data:
    print(row)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import time

# # Initialize WebDriver
# driver = webdriver.Chrome()

# # Define the URL
# url = "https://www.icra.in/Rating/RatingCategory?RatingType=CR&RatingCategoryId=5"
# driver.get(url)

# # Function to extract data from the current page
# def extract_data():
#     # Wait for the table to be present
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'entity_data_table')))

#     # Extract the page source after the table is loaded
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     table = soup.find('table', {'id': 'entity_data_table'})
#     rows = table.find_all('tr')
#     data = []
#     for row in rows:
#         cells = row.find_all('td')
#         data.append([cell.text.strip() for cell in cells])
#     return data

# # List to store all data
# all_data = []

# # Loop through pages and extract data
# for page in range(1, 11):  # Adjusted to limit to 10 pages
#     print(f"Scraping page {page}")
#     page_data = extract_data()

#     # Ensure we only add unique data
#     for data_row in page_data:
#         if data_row not in all_data and data_row != []:
#             all_data.append(data_row)

#     # Click the next button
#     try:
#         next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="contentPager"]/div/ul/li[5]/a')))
#         driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
#         time.sleep(1)  # Adjusted delay to 1 second
#         next_button.click()
#         time.sleep(5)  # Adjusted delay to 5 seconds
#     except Exception as e:
#         print(f"Failed to navigate to the next page: {e}")
#         break

# # Close the WebDriver
# driver.quit()

# # Print the data
# for row in all_data:
#     print(row)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup
# import time

# # Initialize WebDriver
# driver = webdriver.Chrome()

# # Define the URL
# url = "https://www.icra.in/Rating/RatingCategory?RatingType=CR&RatingCategoryId=5"
# driver.get(url)

# # Function to extract data from the current page
# def extract_data():
#     # Wait for the table to be present
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'entity_data_table')))

#     # Extract the page source after the table is loaded
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     table = soup.find('table', {'id': 'entity_data_table'})
#     rows = table.find_all('tr')
#     data = []
#     for row in rows:
#         cells = row.find_all('td')
#         data.append([cell.text.strip() for cell in cells])
#     return data

# # List to store all data
# all_data = []

# # Loop through pages and extract data
# for page in range(1, 11):  # Adjusted to limit to 10 pages
#     print(f"Scraping page {page}")
#     page_data = extract_data()

#     # Ensure we only add unique data
#     for data_row in page_data:
#         if data_row not in all_data and data_row != []:
#             all_data.append(data_row)

#     # Click the next button
#     try:
#         next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="contentPager"]/div/ul/li[5]/a')))
#         driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
#         time.sleep(2)
#         next_button.click()
#         time.sleep(5)
#     except Exception as e:
#         print(f"Failed to navigate to the next page: {e}")
#         break

# # Close the WebDriver
# driver.quit()

# # Print the data
# for row in all_data:
#     print(row)


