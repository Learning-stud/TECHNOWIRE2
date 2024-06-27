

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time


def linkedin(driver, email, password):
    driver.get('https://www.linkedin.com/login')
    email = driver.find_element(By.CLASS_NAME, 'username')
    email.send_keys(email)
    password = driver.find_element(By.CLASS_NAME, 'password')
    password.send_keys(password)
    login = driver.find_element(By.CLASS_NAME, 'submit-button')
    login.click()
def extractPdf(driver):
    pdfLink = []
    a_tags = driver.find_elements(By.TAG_NAME, 'a')

    for a_tag in a_tags:
        href = a_tag.get_attribute('href')
        if href and href.endswith('.pdf'):
            pdfLink.append(href)
    return pdfLink

service = Service('selenium_scrapping/chromedriver.exe')
driver = webdriver.Chrome(service=service)
user_email = 'jayahalpara123456@gmail.com'
user_password = 'jaygajjar@123'

try:

    linkedin(driver, user_email, user_password)
    profile = 'https://www.linkedin.com/in/dr-vaishali-dixit-803156264/recent-activity/all/'
    driver.get(profile)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    while True:
        try:
            showMore = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ssplayer-virus-scan-container__download-button')))
            showMore.click()
            time.sleep(2)
        except (NoSuchElementException, TimeoutException):
            break
    pdfLink = extractPdf(driver)

    for pdf_link in pdfLink:
        print(pdf_link)
finally:
    driver.quit()
