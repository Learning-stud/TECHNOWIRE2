# import time
# import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from bs4 import BeautifulSoup

# driver = webdriver.Chrome()

# url = "https://www.bcregistry.org.in/iba/home/HomeAction.do?doBCPortal=yes"
# driver.get(url)

# try:
#     state = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="stateId"]')))
#     Select(state).select_by_value('14')

#     district = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="districtId"]')))
#     Select(district).select_by_value('153')

#     acess = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="nav-main1"]/ul/div/div/div[3]/div/div/a')))
#     driver.execute_script("arguments[0].click();", acess)

#     WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'table')))

#     soup = BeautifulSoup(driver.page_source, 'html.parser')

#     table = soup.find('table', class_='table table-hover table-light')

#     with open('..\Haryana--Rohtak.csv', mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['bc_name', 'mobile_no', 'pincode', 'bank_name'])

#         try:
#             rows = table.find_all('tr')

#             for row in rows:
#                 columns = row.find_all('td')
#                 if columns:
#                     bc_name = columns[1].text.strip()
#                     mobile_no = columns[2].text.strip()
#                     pincode = columns[3].text.strip()
#                     bank_name = columns[4].text.strip()

#                     href = columns[1].find('a')['href'] if columns[1].find('a') else None

#                     writer.writerow([bc_name, mobile_no, pincode, bank_name])

#                     print(f"{bc_name}, {mobile_no}, {pincode}, {bank_name}")

#         except Exception as e:
#             print(f"Error occurred during data extraction: {str(e)}")

#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-body')))

#     captcha_element = driver.find_element(By.CLASS_NAME, 'captcha_text')
#     captcha_text = captcha_element.text.strip()

#     captcha_input = driver.find_element(By.ID, 'cap_search')
#     captcha_input.clear()
#     captcha_input.send_keys(captcha_text)

#     verify_button = driver.find_element(By.CLASS_NAME, 'btn.blue')
#     driver.execute_script("arguments[0].click();", verify_button)

#     time.sleep(10)

# except Exception as e:
#     print(f"Error occurred: {str(e)}")

# finally:
#     driver.quit()




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

district_values = ['157', '158', '159', '160', '161', '162', '777', '164', '165', '166', '167', '168']

def save_data(district_value):
    try:
        # Select the state
        state = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="stateId"]')))
        Select(state).select_by_value('15')  # Himachal Pradesh value

        # Select the district
        district = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="districtId"]')))
        Select(district).select_by_value(district_value)

        # Click the access button
        access = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="nav-main1"]/ul/div/div/div[3]/div/div/a')))
        driver.execute_script("arguments[0].click();", access)

        # Wait for the captcha to be present
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, 'captcha_text')))

        # Wait for user to input the captcha manually
        input("Please enter the captcha and press Enter to continue...")

        # Wait for the table to be present
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'table')))

        # Parse the page with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find('table', class_='table table-hover table-light')

        # Open a CSV file to write the data
        with open(f'./Himachal_Pradesh--District_{district_value}.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['bc_name', 'mobile_no', 'pincode', 'bank_name'])

            try:
                rows = table.find_all('tr')
                for row in rows:
                    columns = row.find_all('td')
                    if columns:
                        bc_name = columns[1].text.strip()
                        mobile_no = columns[2].text.strip()
                        pincode = columns[3].text.strip()
                        bank_name = columns[4].text.strip()

                        writer.writerow([bc_name, mobile_no, pincode, bank_name])

                        print(f"{bc_name}, {mobile_no}, {pincode}, {bank_name}")

            except Exception as e:
                print(f"Error occurred during data extraction: {str(e)}")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

for district_value in district_values:
    save_data(district_value)
    time.sleep(20)  # To prevent too fast requests and potential blocking

driver.quit()