

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

    # Find the email input field by class name and enter the email
    email_element = driver.find_element(By.CLASS_NAME, 'username')
    email_element.send_keys(email)

    # Find the password input field by class name and enter the password
    password_element = driver.find_element(By.CLASS_NAME, 'password')
    password_element.send_keys(password)

    # Find the login button by class name and click it to log in
    login_button = driver.find_element(By.CLASS_NAME, 'submit-button')
    login_button.click()

# Function to extract PDF links from the current page
def extract_pdf_links(driver):
    pdf_links = []
    # Find all <a> tags on the page
    a_tags = driver.find_elements(By.TAG_NAME, 'a')
    # Loop through each <a> tag to check for PDF links
    for a_tag in a_tags:
        href = a_tag.get_attribute('href')  # Get the href attribute of the <a> tag
        if href and href.endswith('.pdf'):  # Check if the href ends with .pdf
            pdf_links.append(href)  # Add the PDF link to the list
    return pdf_links



# Initialize WebDriver (Chrome in this case)
service = Service('selenium scrapping/chromedriver.exe')  # Path to the chromedriver executable
driver = webdriver.Chrome(service=service)  # Create a new Chrome session

# LinkedIn login credentials
email = 'jayahalpara123456@gmail.com'
password = 'jaygajjar@123'

try:
    # Log in to LinkedIn
    linkedin_login(driver, email, password)

    # Navigate to the LinkedIn profile page
    profile_url = 'https://www.linkedin.com/in/dr-vaishali-dixit-803156264/recent-activity/all/'  # URL of the LinkedIn profile
    driver.get(profile_url)

    # Wait until the page loads by checking the presence of the body tag
    wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Click "Show More" buttons if available
    while True:
        try:
            # Wait until the "Show More" button is clickable and click it
            show_more_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ssplayer-virus-scan-container__download-button')))
            show_more_button.click()
            time.sleep(2)  # Wait for the content to load after clicking
        except (NoSuchElementException, TimeoutException):
            # Exit the loop if there are no more "Show More" buttons
            break

    # Extract PDF links from the profile page
    pdf_links = extract_pdf_links(driver)

    # Print the extracted PDF links
    for pdf_link in pdf_links:
        print(pdf_link)

finally:
    # Close the WebDriver session
    driver.quit()
