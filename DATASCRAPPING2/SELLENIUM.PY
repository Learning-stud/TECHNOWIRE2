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
# # # import concurrent.futures
# # # import requests
# # # from bs4 import BeautifulSoup

# # # # Function to fetch and parse data from a single page
# # # def fetch_page_data(page):
# # #     url = "https://www.icra.in/Rating/RatingCategory?RatingType=CR&RatingCategoryId=5"
# # #     params = {'pageIndex': page}
# # #     response = requests.get(url, params=params)
# # #     response.raise_for_status()

# # #     soup = BeautifulSoup(response.text, 'html.parser')
# # #     table = soup.find('table', {'id': 'entity_data_table '})
# # #     rows = table.find_all('tr')
# # #     data = []
# # #     for row in rows:
# # #         cells = row.find_all('td')
# # #         data.append([cell.text.strip() for cell in cells])
# # #     return data

# # # # Main script to fetch data concurrently
# # # def main():
# # #     all_data = []
# # #     page_limit = 10  # Define the number of pages to fetch

# # #     with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
# # #         futures = [executor.submit(fetch_page_data, page) for page in range(1, page_limit + 1)]
# # #         for future in concurrent.futures.as_completed(futures):
# # #             all_data.extend(future.result())

# # #     # Print the collected data
# # #     for row in all_data:
# # #         print(row)

# # # if __name__ == "__main__":
# # #     import time
# # #     start_time = time.time()

# # #     main()

# # #     end_time = time.time()
# # #     print(f"Data fetched in {end_time - start_time:.2f} seconds")
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from bs4 import BeautifulSoup
# # import time
# # from threading import Thread, Lock

# # driver = webdriver.Chrome()
# # url = "https://www.icra.in/Rating/RatingCategory?RatingType=CR&RatingCategoryId=5"
# # driver.get(url)

# # # Global data storage with a lock for thread-safe operations
# # all_data = []
# # data_lock = Lock()

# # # Function to extract data from the current page
# # def extract_data():
# #     WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'entity_data_table')))
# #     soup = BeautifulSoup(driver.page_source, 'html.parser')
# #     table = soup.find('table', {'id': 'entity_data_table'})
# #     rows = table.find_all('tr')
# #     data = []
# #     for row in rows:
# #         cells = row.find_all('td')
# #         row_data = [cell.text.strip() for cell in cells]
# #         if row_data:  # Only append non-empty rows
# #             data.append(row_data)
# #     return data

# # # Function to scrape data from a given page
# # def scrape_page(page_number):
# #     try:
# #         page_url = f"{url}&Page={page_number}"
# #         driver.get(page_url)
# #         page_data = extract_data()
# #         with data_lock:
# #             for data_row in page_data:
# #                 if data_row not in all_data:  # Avoid duplicates
# #                     all_data.append(data_row)
# #     except Exception as e:
# #         print(f"Failed to scrape page {page_number}: {e}")

# # # Main scraping function using threading
# # def main_scraping(page_limit):
# #     threads = []
# #     for page_number in range(1, page_limit + 1):
# #         thread = Thread(target=scrape_page, args=(page_number,))
# #         threads.append(thread)
# #         thread.start()

# #     for thread in threads:
# #         thread.join()

# # # Number of pages to scrape
# # page_limit = 20

# # # Start the scraping process
# # start_time = time.time()
# # main_scraping(page_limit)
# # end_time = time.time()

# # # Close the driver
# # driver.quit()

# # # Print the collected data
# # for row in all_data:
# #     print(row)

# # print(f"Scraping completed in {end_time - start_time} seconds")




# import requests

# # Endpoint URL (replace with the actual one found in Network tab)
# endpoint_url = 'https://www.google.com/recaptcha/api2/'


# # https://www.google.com/recaptcha/api.js
# # Headers (if required)
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Accept': 'application/json, text/plain, */*',
# }

# # Parameters
# params = {
#     'RatingType': 'CR',
#     'RatingCategoryId': 5,
# }

# # Fetching the data
# response = requests.get(endpoint_url, headers=headers, params=params)

# if response.status_code == 200:
#     data = response.json()  # Assuming JSON response
#     for item in data:
#         print(item)
# else:
#     print(f"Failed to fetch data: {response.status_code}")