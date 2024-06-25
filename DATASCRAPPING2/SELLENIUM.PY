


import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)

def extract_data(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'entity_data_table')))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find('table', {'id': 'entity_data_table'})
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cells = row.find_all('td')
        row_data = [cell.text.strip() for cell in cells]
        if row_data:
            data.append(row_data)
    return data

def click_next(driver):
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="contentPager"]//li[@class="PagedList-skipToNext"]/a'))
        )
        driver.execute_script("arguments[0].click();", next_button)
        WebDriverWait(driver, 10).until(EC.staleness_of(next_button))
    except Exception as e:
        print(f"Exception while clicking next: {e}")
        return False
    return True

def scrape_pages(start_page, end_page, all_data, lock):
    driver = setup_driver()
    url = "https://www.icra.in/Rating/RatingCategory?RatingType=CR&RatingCategoryId=5"
    driver.get(url)

    for _ in range(start_page):
        if not click_next(driver):
            driver.quit()
            return

    for _ in range(end_page - start_page):
        data = extract_data(driver)
        with lock:
            for data_row in data:
                if data_row not in all_data:
                    all_data.append(data_row)
        if not click_next(driver):
            break

    driver.quit()

def concurrent_scrape(page_limit, num_threads):
    all_data = []
    lock = threading.Lock()
    threads = []
    pages_per_thread = (page_limit + num_threads - 1) // num_threads  # Calculate pages per thread ensuring coverage of all pages

    for i in range(num_threads):
        start_page = i * pages_per_thread
        end_page = min((i + 1) * pages_per_thread, page_limit)  # Ensure we don't exceed the page limit
        thread = threading.Thread(target=scrape_pages, args=(start_page, end_page, all_data, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return all_data

# Define the number of pages to scrape and the number of threads
page_limit = 20
num_threads = 10
all_data = concurrent_scrape(page_limit, num_threads)

# Print the extracted data
for row in all_data:
    print(row)



