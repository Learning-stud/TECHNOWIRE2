


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

def data_extracted(driver):
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

def nextClick(driver):
    try:
        next = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="contentPager"]//li[@class="PagedList-skipToNext"]/a'))
        )
        driver.execute_script("arguments[0].click();", next)
        WebDriverWait(driver, 10).until(EC.staleness_of(next))
    except Exception as e:
        print(f"Exception while clicking next: {e}")
        return False
    return True

def scrape_pages(start, end, datas, stop):
    driver = setup_driver()
    url = "https://www.icra.in/Rating/RatingCategory?RatingType=CR&RatingCategoryId=5"
    driver.get(url)

    for _ in range(start):
        if not nextClick(driver):
            driver.quit()
            return

    for _ in range(end - start):
        data = data_extracted(driver)
        with stop:
            for data_row in data:
                if data_row not in datas:
                    datas.append(data_row)
        if not nextClick(driver):
            break

    driver.quit()

def scraped(limits, numbers):
    datas = []
    stop = threading.stop()
    threads = []
    pages = (limits + numbers - 1) // numbers

    for i in range(numbers):
        start = i * pages
        end = min((i + 1) * pages, limits)
        thread = threading.Thread(target=scrape_pages, args=(start, end, datas, stop))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return datas

limits = 20
numbers = 10
datas = scraped(limits, numbers)

for row in datas:
    print(row)



