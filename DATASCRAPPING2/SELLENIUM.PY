# WORKING PERFECT

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()

url = "https://www.icra.in/Rating/RatingCategory?RatingType=CR&RatingCategoryId=5"
driver.get(url)
def extract_data():
    print("Waiting for entity_data_table to be present...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'entity_data_table')))
    print("entity_data_table found, extracting data...")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find('table', {'id': 'entity_data_table'})
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cells = row.find_all('td')
        row_data = [cell.text.strip() for cell in cells]
        data.append(row_data)
        print(f"Extracted row data: {row_data}")
    print(f"Extracted {len(data)} rows of data")
    return data

        # """
        # Extracts data from a web page using Selenium and BeautifulSoup.

        # This function waits for the 'entity_data_table' element to be present on the page, then extracts the data from the table.
        # It finds the table element by its ID, then iterates over each row in the table and extracts the text from each cell.
        # The extracted data is stored in a list of lists, where each inner list represents a row of data.
        # The function prints each row of data as it is extracted and also prints the total number of rows extracted.
        # Finally, the function returns the extracted data as a list of lists.

        # Returns:
        #     list: A list of lists, where each inner list represents a row of data.
        # """
all_data = []
def scrape_page_data():
    print("Scraping page data...")
    page_data = extract_data()
    print(f"Extracted {len(page_data)} rows of data")
    for data_row in page_data:
        if data_row not in all_data and data_row != []:
            print(f"Appending row data: {data_row}")
            all_data.append(data_row)
scrape_page_data()



'''
    Scrapes page data by extracting data from a web page using Selenium and BeautifulSoup.
    This function waits for the 'entity_data_table' element to be present on the page, then extracts the data from the table.
    It finds the table element by its ID, then iterates over each row in the table and extracts the text from each cell.
    The extracted data is stored in a list of lists, where each inner list represents a row of data.
    The function prints each row of data as it is extracted and also prints the total number of rows extracted.
    Finally, the function appends each row of data to the 'all_data' list if it is not already present in the list and not an empty list.
    This function does not return anything.

    Parameters:
        None

    Returns:
        None
'''
page_limit = 10
current_page = 1

while current_page < page_limit:
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="contentPager"]//li[@class="PagedList-skipToNext"]/a'))
        )
        print(f"Next button text: {next_button.text}")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
        time.sleep(5)
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(5)
        WebDriverWait(driver, 10).until(EC.staleness_of(next_button))
        scrape_page_data()
        current_page += 1
    except Exception as e:
        print(f"Failed to navigate to the next page: {e}")
        break
driver.quit()
for row in all_data:
    print(row)

# Function to fetch data from the API
# import concurrent.futures
# import requests
# from bs4 import BeautifulSoup

# # Function to fetch and parse data from a single page
# def fetch_page_data(page):
#     url = "https://www.icra.in/Rating/RatingCategory?RatingType=CR&RatingCategoryId=5"
#     params = {'pageIndex': page}
#     response = requests.get(url, params=params)
#     response.raise_for_status()

#     soup = BeautifulSoup(response.text, 'html.parser')
#     table = soup.find('table', {'id': 'entity_data_table '})
#     rows = table.find_all('tr')
#     data = []
#     for row in rows:
#         cells = row.find_all('td')
#         data.append([cell.text.strip() for cell in cells])
#     return data

# # Main script to fetch data concurrently
# def main():
#     all_data = []
#     page_limit = 10  # Define the number of pages to fetch

#     with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#         futures = [executor.submit(fetch_page_data, page) for page in range(1, page_limit + 1)]
#         for future in concurrent.futures.as_completed(futures):
#             all_data.extend(future.result())

#     # Print the collected data
#     for row in all_data:
#         print(row)

# if __name__ == "__main__":
#     import time
#     start_time = time.time()

#     main()

#     end_time = time.time()
#     print(f"Data fetched in {end_time - start_time:.2f} seconds")
