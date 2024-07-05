# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import mysql.connector
# from bs4 import BeautifulSoup

# # Function to connect to MySQL database
# def connect_to_mysql():
#     try:
#         conn = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='Jy%02kl&R@bh',
#             database='bc_bank'
#         )
#         if conn.is_connected():
#             print('Connected to MySQL database')
#             return conn
#     except mysql.connector.Error as e:
#         print(f"Error connecting to MySQL database: {e}")
#         return None

# driver = webdriver.Chrome()

# # URL of the page
# url = "https://www.bcregistry.org.in/iba/home/HomeAction.do?doBCPortal=yes"

# # Open the page
# driver.get(url)

# # Wait for the table to load (adjust timeout as needed)
# WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'table')))

# # Parse the HTML with BeautifulSoup
# soup = BeautifulSoup(driver.page_source, 'html.parser')

# # Find the table containing the data
# table = soup.find('table', class_='table table-hover table-light')

# # Connect to MySQL database
# conn = connect_to_mysql()
# if not conn:
#     driver.quit()
#     exit()

# # Create a cursor object using the connection
# cursor = conn.cursor()

# try:
#     # Find all rows in the table
#     rows = table.find_all('tr')

#     for row in rows:
#         # Extract data from each row
#         columns = row.find_all('td')
#         if columns:
#             # Extract specific data
#             bc_name = columns[1].text.strip()
#             mobile_no = columns[2].text.strip()
#             pincode = columns[3].text.strip()
#             bank_name = columns[4].text.strip()

#             # Extract href attribute from the anchor tag within bc_name
#             href = columns[1].find('a')['href'] if columns[1].find('a') else None

#             # Insert data into MySQL table
#             insert_query = "INSERT INTO bc_details (bc_name, mobile_no, pincode, bank_name, href) VALUES (%s, %s, %s, %s, %s)"
#             data = (bc_name, mobile_no, pincode, bank_name, href)
#             cursor.execute(insert_query, data)
#             conn.commit()

#             print(f"Inserted: {bc_name}, {mobile_no}, {pincode}, {bank_name}, {href}")

# except Exception as e:
#     print(f"Error occurred during data insertion: {str(e)}")

# finally:
#     # Close cursor and connection
#     cursor.close()
#     conn.close()

#     # Close the browser
#     driver.quit()

# # Fetch data from MySQL (optional step)
# def fetch_data_from_mysql():
#     conn = connect_to_mysql()
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

# connect to MySQL database
def connect_to_mysql():
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

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome to avoid opening a browser window
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# URL of the page
url = "https://www.bcregistry.org.in/iba/home/HomeAction.do?doBCPortal=yes"

# Open the page
driver.get(url)

#  "Gujarat"
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stateId"]')))
select_state = Select(driver.find_element(By.XPATH, '//*[@id="stateId"]'))
select_state.select_by_visible_text('Gujarat')

#  "Ahemdabad"
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="districtId"]/option[2]')))
district_select = Select(driver.find_element(By.XPATH, '//*[@id="districtId"]'))
district_select.select_by_index(1)

# search
search_button = driver.find_element(By.XPATH, '//*[@id="nav-main1"]/ul/div/div/div[3]/div/div/a')
search_button.click()

# captcha modal
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="txtCaptcha_search"]')))

#  captcha input
captcha_text = driver.find_element(By.XPATH, '//*[@id="txtCaptcha_search"]').text
captcha_input = driver.find_element(By.XPATH, '//*[@id="cap_search"]')
captcha_input.send_keys(captcha_text)

#  button
verify_button = driver.find_element(By.XPATH, '//*[@id="searchmodal"]/div/div/div/div/div[3]/a')
verify_button.click()

# table to load
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'table')))

#  HTML with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

#table containing the data
table = soup.find('table', class_='table table-hover table-light')

# MySQL database
conn = connect_to_mysql()
if not conn:
    driver.quit()
    exit()

# cursor object using the connection
cursor = conn.cursor()

try:
    #  all rows in the table
    rows = table.find_all('tr')

    for row in rows:
        #  data from each row
        columns = row.find_all('td')
        if columns:
            #  specific data
            bc_name = columns[1].text.strip()
            mobile_no = columns[2].text.strip()
            pincode = columns[3].text.strip()
            bank_name = columns[4].text.strip()

            #  href attribute from the anchor tag within bc_name
            href = columns[1].find('a')['href'] if columns[1].find('a') else None

            # Insert data into MySQL table
            insert_query = "INSERT INTO bc_details (bc_name, mobile_no, pincode, bank_name, href) VALUES (%s, %s, %s, %s, %s)"
            data = (bc_name, mobile_no, pincode, bank_name, href)
            cursor.execute(insert_query, data)
            conn.commit()

            print(f"Inserted: {bc_name}, {mobile_no}, {pincode}, {bank_name}, {href}")

except Exception as e:
    print(f"Error occurred during data insertion: {str(e)}")

finally:
    cursor.close()
    conn.close()
    driver.quit()

#  data from MySQL (optional step)
def fetch_data_from_mysql():
    conn = connect_to_mysql()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM bc_details")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except mysql.connector.Error as e:
        print(f"Error fetching data: {e}")

    finally:
        cursor.close()
        conn.close()

fetch_data_from_mysql()
