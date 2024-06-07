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
    for row in rows:
        cells = row.find_all('td')
        data.append([cell.text.strip() for cell in cells])
    return data

# List to store all data
all_data = []

# Loop through pages and extract data
for page in range(1, 5):  # Adjust the range according to the total number of pages
    print(f"Scraping page {page}")
    all_data.extend(extract_data())
    try:
        # Find and click the 'Next' button using XPath or a more reliable selector
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Next")]'))
        )
        next_button.click()
        time.sleep(20)  # Adjust sleep time if necessary
    except Exception as e:
        print(f"Failed to navigate to the next page: {e}")
        break

# Close the WebDriver
driver.quit()

# Print the data
for row in all_data:
    print(row)



