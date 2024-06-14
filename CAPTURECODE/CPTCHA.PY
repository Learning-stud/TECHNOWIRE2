from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pytesseract
from PIL import Image

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with your path

# Set up Selenium WebDriver using Service
service = Service(r'C:\selenium_scrapping\chromedriver.exe')  # Update with your path
driver = webdriver.Chrome(service=service)

# Open the website
driver.get('https://einvoice1.gst.gov.in/Home/UserRegistration')

# Locate the CAPTCHA image element
captcha_element = driver.find_element(By.XPATH, '//*[@id="captcha_image"]')

# Save the CAPTCHA image
captcha_image_path = 'captcha.png'
captcha_element.screenshot(captcha_image_path)

# Use Tesseract OCR to extract text from the CAPTCHA image
captcha_text = pytesseract.image_to_string(Image.open(captcha_image_path)).strip()

# Locate the CAPTCHA input field and enter the extracted CAPTCHA text
captcha_input = driver.find_element(By.XPATH, '//*[@id="txtCaptchaCode"]')
captcha_input.send_keys(captcha_text)

# Fill other form fields as required
# Example (assuming you need to fill username):
# username_input = driver.find_element(By.ID, 'username_field_id')
# username_input.send_keys('your_username')

# Submit the form
submit_button = driver.find_element(By.ID, 'btngo')  # Replace with the actual ID of the submit button
submit_button.click()

# Wait for a while to see the result
time.sleep(5)

# Close the browser
driver.quit()
