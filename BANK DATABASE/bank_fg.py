
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import mysql.connector
from bs4 import BeautifulSoup

def mysql_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Jy%02kl&R@bh',
            database='bc_bank'
        )
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

driver = webdriver.Chrome()

# URL of the page
url = "https://www.bcregistry.org.in/iba/home/HomeAction.do?doBCPortal=yes"

driver.get(url)

try:
    state_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="stateId"]')))
    Select(state_dropdown).select_by_value('10')  # Select Gujarat

    district_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="districtId"]')))
    Select(district_dropdown).select_by_index(2)

    go_button = driver.find_element(By.XPATH, '//*[@id="nav-main1"]/ul/div/div/div[3]/div/div/a')
    go_button.click()

    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'table')))

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    table = soup.find('table', class_='table table-hover table-light')

    conn = mysql_connection()
    if not conn:
        driver.quit()
        exit()

    cursor = conn.cursor()

    try:
        rows = table.find_all('tr')

        for row in rows:
            columns = row.find_all('td')
            if columns:
                bc_name = columns[1].text.strip()
                mobile_no = columns[2].text.strip()
                pincode = columns[3].text.strip()
                bank_name = columns[4].text.strip()

                href = columns[1].find('a')['href'] if columns[1].find('a') else None

                # insert_query = "INSERT INTO bc_details (bc_name, mobile_no, pincode, bank_name, href) VALUES (%s, %s, %s, %s, %s)"
                # data = (bc_name, mobile_no, pincode, bank_name, href)
                # cursor.execute(insert_query, data)
                conn.commit()

    #             print(f"Inserted: {bc_name}, {mobile_no}, {pincode}, {bank_name}, {href}")

    except Exception as e:
        print(f"Error occurred during data insertion: {str(e)}")

    finally:
        cursor.close()
        conn.close()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-body')))

    captcha_element = driver.find_element(By.CLASS_NAME, 'captcha_text')
    captcha_text = captcha_element.text.strip()

    captcha_input = driver.find_element(By.ID, 'cap_search')
    captcha_input.clear()
    captcha_input.send_keys(captcha_text)

    verify_button = driver.find_element(By.CLASS_NAME, 'btn.blue')
    verify_button.click()


    time.sleep(5)

except Exception as e:
    print(f"Error occurred: {str(e)}")

finally:
    driver.quit()

# Function to fetch and print data from MySQL
# def fetch_data_from_mysql():
#     conn = mysql_connection()
#     if not conn:
#         return

#     cursor = conn.cursor()
#     try:
#         cursor.execute("SELECT * FROM bc_details")
#         rows = cursor.fetchall()

#         for row in rows:
#             print(row)

#     except mysql.connector.Error as e:
#         print(f"Error fetching data: {e}")

#     finally:
#         cursor.close()
#         conn.close()

# # Fetch and print the data from MySQL database
# fetch_data_from_mysql()
