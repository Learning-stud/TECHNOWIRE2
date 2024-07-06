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
# def mysql_connection():
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
# conn = mysql_connection()
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

# fetch_data_from_mysql()
#       =====================================================================Rujal Script ============================================================================


# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# import mysql.connector
# from bs4 import BeautifulSoup

# # Function to connect to MySQL database
# def mysql_connection():
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

# # Initialize the WebDriver without headless mode
# driver = webdriver.Chrome()

# # URL of the page
# url = "https://www.bcregistry.org.in/iba/home/HomeAction.do?doBCPortal=yes"

# # Open the page
# driver.get(url)

# try:
#     # Wait for the State dropdown to be interactive and select Gujarat
#     state_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="stateId"]')))
#     Select(state_dropdown).select_by_value('12')  # Select Gujarat

#     # Wait for the District dropdown to be interactive and select Ahmedabad
#     district_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="districtId"]')))
#     Select(district_dropdown).select_by_index(1)  # Select Ahmedabad

#     # Click the Go button
#     go_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-main1"]/ul/div/div/div[3]/div/div/a')))
#     go_button.click()

#     # Wait for the table to load (adjust timeout as needed)
#     WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'table')))

#     # Parse the HTML with BeautifulSoup
#     soup = BeautifulSoup(driver.page_source, 'html.parser')

#     # Find the table containing the data
#     table = soup.find('table', class_='table table-hover table-light')

#     # Connect to MySQL database
#     conn = mysql_connection()
#     if not conn:
#         driver.quit()
#         exit()

#     # Create a cursor object using the connection
#     cursor = conn.cursor()

#     try:
#         # Find all rows in the table
#         rows = table.find_all('tr')

#         for row in rows:
#             # Extract data from each row
#             columns = row.find_all('td')
#             if columns:
#                 # Extract specific data
#                 bc_name = columns[1].text.strip()
#                 mobile_no = columns[2].text.strip()
#                 pincode = columns[3].text.strip()
#                 bank_name = columns[4].text.strip()

#                 # Extract href attribute from the anchor tag within bc_name
#                 href = columns[1].find('a')['href'] if columns[1].find('a') else None

#                 # Insert data into MySQL table
#                 insert_query = "INSERT INTO bc_details (bc_name, mobile_no, pincode, bank_name, href) VALUES (%s, %s, %s, %s, %s)"
#                 data = (bc_name, mobile_no, pincode, bank_name, href)
#                 cursor.execute(insert_query, data)
#                 conn.commit()

#                 print(f"Inserted: {bc_name}, {mobile_no}, {pincode}, {bank_name}, {href}")

#     except Exception as e:
#         print(f"Error occurred during data insertion: {str(e)}")

#     finally:
#         # Close cursor and connection
#         cursor.close()
#         conn.close()

# except Exception as e:
#     print(f"Error occurred: {str(e)}")

# finally:
#     # Close the browser
#     driver.quit()

# # Function to fetch data from MySQL
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
#================================================================= Mine Script upto go button========================================================================
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

# Function to connect to MySQL database
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

# Initialize the WebDriver without headless mode
driver = webdriver.Chrome()

# URL of the page
url = "https://www.bcregistry.org.in/iba/home/HomeAction.do?doBCPortal=yes"

driver.get(url)

try:
    # Wait for the State dropdown to be interactive
    state_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="stateId"]')))
    Select(state_dropdown).select_by_value('10')  # Select Gujarat

    # Wait for the District dropdown to be interactive
    district_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="districtId"]')))
    Select(district_dropdown).select_by_index(2)  # Select Ahmedabad

    # Click the Go button
    go_button = driver.find_element(By.XPATH, '//*[@id="nav-main1"]/ul/div/div/div[3]/div/div/a')
    go_button.click()

    # Wait for the table to load
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'table')))

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the table containing the data
    table = soup.find('table', class_='table table-hover table-light')

    # Connect to MySQL database
    conn = mysql_connection()
    if not conn:
        driver.quit()
        exit()

    cursor = conn.cursor()

    try:
        # Find all rows in the table
        rows = table.find_all('tr')

        for row in rows:
            # Extract data from each row
            columns = row.find_all('td')
            if columns:
                # Extract specific data
                bc_name = columns[1].text.strip()
                mobile_no = columns[2].text.strip()
                pincode = columns[3].text.strip()
                bank_name = columns[4].text.strip()

                # Extract href attribute from the anchor tag within bc_name
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
        # Close cursor and connection
        cursor.close()
        conn.close()

    # Handle Captcha
    # Wait for modal to appear
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-body')))

    # Find captcha text element
    captcha_element = driver.find_element(By.CLASS_NAME, 'captcha_text')
    captcha_text = captcha_element.text.strip()

    # Input captcha text into the input field
    captcha_input = driver.find_element(By.ID, 'cap_search')
    captcha_input.clear()  # Clear existing input
    captcha_input.send_keys(captcha_text)

    # Click the verify button
    verify_button = driver.find_element(By.CLASS_NAME, 'btn.blue')
    verify_button.click()

    # Wait for a while (for demonstration purposes)
    time.sleep(5)  # Wait for 5 seconds

except Exception as e:
    print(f"Error occurred: {str(e)}")

finally:
    # Close the browser
    driver.quit()

# Function to fetch and print data from MySQL
def fetch_data_from_mysql():
    conn = mysql_connection()
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

# Fetch and print the data from MySQL database
fetch_data_from_mysql()
