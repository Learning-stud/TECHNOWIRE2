# WORKING PERFECT 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Define the URL
url = "https://www.icra.in/Rating/RatingCategory?RatingType=CR&RatingCategoryId=5"
driver.get(url)

# Function to extract data from the current page
def extract_data():
    # Wait for the table to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'entity_data_table')))

    # Extract the page source after the table is loaded
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

# Define a function to scrape data from the current page and append it to all_data
def scrape_page_data():
    page_data = extract_data()
    # Ensure we only add unique data
    for data_row in page_data:
        if data_row not in all_data and data_row != []:
            all_data.append(data_row)

# Scrape data from the first page
scrape_page_data()

# Set the page limit
page_limit = 10
current_page = 1

# Find and click the "Next" button to navigate to the next page
while current_page < page_limit:
    try:
        # Locate the "Next" button using a more robust XPath
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="contentPager"]//li[@class="PagedList-skipToNext"]/a'))
        )

        # Print the "Next" button text for debugging
        print(f"Next button text: {next_button.text}")

        # Scroll the next button into view
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
        time.sleep(2)

        # Use JavaScript to click the button
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(5)  # Adjust sleep time if necessary

        # Wait for the new page to load
        WebDriverWait(driver, 10).until(EC.staleness_of(next_button))

        # Scrape data from the new page
        scrape_page_data()

        # Increment the page counter
        current_page += 1
    except Exception as e:
        print(f"Failed to navigate to the next page: {e}")
        break

# Close the WebDriver
driver.quit()

# Print the data
for row in all_data:
    print(row)


#--------------------------------------------------------- FINALLY DONE -----------------------------------------------------------------------
