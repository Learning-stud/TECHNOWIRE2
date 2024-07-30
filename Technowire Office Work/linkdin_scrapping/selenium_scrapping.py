

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Function to log in to LinkedIn
def linkedin_login(driver, email, password):
    # Open LinkedIn login page
    driver.get('https://www.linkedin.com/login')

    email_element = driver.find_element(By.CLASS_NAME, 'username')
    email_element.send_keys(email)

    password_element = driver.find_element(By.CLASS_NAME, 'password')
    password_element.send_keys(password)

    login_button = driver.find_element(By.CLASS_NAME, 'submit-button')
    login_button.click()

def extract_pdf_links(driver):
    pdf_links = []
    a_tags = driver.find_elements(By.TAG_NAME, 'a')
    for a_tag in a_tags:
        href = a_tag.get_attribute('href')
        if href and href.endswith('.pdf'):
            pdf_links.append(href)
    return pdf_links


service = Service('chromedriver.exe')

service = Service('path/to/chromedriver')
driver = webdriver.Chrome(service=service)

email = 'jayahalpara123456@gmail.com'
password = 'jaygajjar@123'

try:
    # Log in to LinkedIn
    linkedin_login(driver, email, password)

    profile_url = 'https://www.linkedin.com/in/dr-vaishali-dixit-803156264/recent-activity/all/'
    driver.get(profile_url)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    while True:
        try:
            show_more_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ssplayer-virus-scan-container__download-button')))
            show_more_button.click()
            time.sleep(2)
        except (NoSuchElementException, TimeoutException):
            break

    pdf_links = extract_pdf_links(driver)

    for pdf_link in pdf_links:
        print(pdf_link)

finally:
    driver.quit()
