import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

url = "https://www.bcregistry.org.in/iba/home/HomeAction.do?doBCPortal=yes"

driver.get(url)

try:
    state = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="stateId"]')))
    Select(state).select_by_value('5')

    district = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="districtId"]')))
    Select(district).select_by_value('6')


    acess = driver.find_element(By.XPATH, '//*[@id="nav-main1"]/ul/div/div/div[3]/div/div/a')
    acess.click()


    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'table')))


    soup = BeautifulSoup(driver.page_source, 'html.parser')


    table = soup.find('table', class_='table table-hover table-light')


    with open('andaman-nicobar-nicobar.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['buisnessCorrespond_name', 'mobile_no', 'pincode', 'bank_name'])

        try:
            rows = table.find_all('tr')

            for row in rows:
                columns = row.find_all('td')
                if columns:
                    buisnessCorrespond_name = columns[1].text.strip()
                    mobile_no = columns[2].text.strip()
                    pincode = columns[3].text.strip()
                    bank_name = columns[4].text.strip()

                    href = columns[1].find('a')['href'] if columns[1].find('a') else None

                    writer.writerow([buisnessCorrespond_name, mobile_no, pincode, bank_name])

                    print(f"{buisnessCorrespond_name}, {mobile_no}, {pincode}, {bank_name}")

        except Exception as e:
            print(f"Error occurred during data extraction: {str(e)}")

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-body')))

    captcha_element = driver.find_element(By.CLASS_NAME, 'captcha_text')
    captcha_text = captcha_element.text.strip()

    captcha_input = driver.find_element(By.ID, 'cap_search')
    captcha_input.clear()
    captcha_input.send_keys(captcha_text)

    verify_button = driver.find_element(By.CLASS_NAME, 'btn.blue')
    verify_button.click()

    time.sleep(10)

except Exception as e:
    print(f"Error occurred: {str(e)}")

finally:
    driver.quit()
