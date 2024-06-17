# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.chrome.service import Service as ChromeService
# # import pytesseract
# # from PIL import Image
# # import time

# # # Warning message for ethical considerations
# # print("WARNING: Automating CAPTCHAs often violates website terms and can be unreliable. Consider using a manual solution or contacting the website owner for an alternative method.")

# # # Function to solve CAPTCHA using OCR
# # def solve_captcha(driver, captcha_element):
# #     # Locate the CAPTCHA image element
# #     captcha_img = driver.find_element(By.XPATH, captcha_element)

# #     # Get the location and size of the CAPTCHA image
# #     location = captcha_img.location
# #     size = captcha_img.size

# #     # Get the screenshot of the entire page
# #     driver.save_screenshot("screenshot.png")

# #     # Crop the CAPTCHA image from the entire screenshot
# #     im = Image.open("screenshot.png")
# #     left = location['x']
# #     top = location['y']
# #     right = location['x'] + size['width']
# #     bottom = location['y'] + size['height']
# #     im = im.crop((left, top, right, bottom))

# #     # Use pytesseract to do OCR on the cropped image
# #     captcha_text = pytesseract.image_to_string(im)

# #     return captcha_text.strip()

# # # Function to fill the form
# # def fill_form(driver, captcha_input_xpath, captcha_text=None):
# #     try:
# #         # Wait for the CAPTCHA input field to be present
# #         captcha_input = WebDriverWait(driver, 10).until(
# #             EC.presence_of_element_located((By.XPATH, captcha_input_xpath))
# #         )

# #         # Solve CAPTCHA using OCR
# #         captcha_text = solve_captcha(driver, '//*[@id="captcha_image"]')

# #         # Fill the CAPTCHA input field
# #         captcha_input.send_keys(captcha_text)

# #         # Rest of your form filling logic here
# #         # Example: driver.find_element(By.ID, "email").send_keys("your_email")

# #     except Exception as e:
# #         print(f"An error occurred: {e}")
# #     finally:
# #         time.sleep(5)  # Adding a short delay before quitting (you may adjust as needed)
# #         driver.quit()

# # if __name__ == "__main__":
# #     # Replace with your WebDriver path
# #     chromedriver_path = "./chromedriver.exe"

# #     # Configure pytesseract path (you need to install Tesseract OCR)
# #     pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'  # Example path

# #     # Initialize Chrome WebDriver
# #     service = ChromeService(executable_path=chromedriver_path)
# #     options = webdriver.ChromeOptions()
# #     options.add_argument("--ignore-certificate-errors")
# #     options.add_argument("--ignore-ssl-errors")
# #     driver = webdriver.Chrome(service=service, options=options)

# #     try:
# #         # Open the webpage with CAPTCHA
# #         driver.get("https://einvoice1.gst.gov.in/Home/UserRegistration")

# #         # Assuming CAPTCHA input ID is `txtCaptchaCode` (replace if necessary)
# #         captcha_input_xpath = '//*[@id="txtCaptchaCode"]'

# #         # Fill the form with the solved CAPTCHA
# #         fill_form(driver, captcha_input_xpath)

# #     except Exception as e:
# #         print(f"An error occurred: {e}")
# #     finally:
# #         driver.quit()
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.chrome.service import Service as ChromeService
# # import pytesseract
# # from PIL import Image, ImageEnhance, ImageFilter
# # import time

# # # Warning message for ethical considerations
# # print("WARNING: Automating CAPTCHAs often violates website terms and can be unreliable. Consider using a manual solution or contacting the website owner for an alternative method.")

# # # Function to preprocess CAPTCHA image for better OCR accuracy
# # def preprocess_image(image_path):
# #     image = Image.open(image_path)
# #     # Convert to grayscale
# #     image = image.convert('L')
# #     # Apply thresholding to get a binary image
# #     image = image.point(lambda x: 0 if x < 140 else 255, '1')
# #     # Apply some filtering to remove noise
# #     image = image.filter(ImageFilter.MedianFilter())
# #     return image

# # # Function to solve CAPTCHA using OCR
# # def solve_captcha(driver, captcha_element):
# #     # Locate the CAPTCHA image element
# #     captcha_img = driver.find_element(By.XPATH, captcha_element)

# #     # Get the location and size of the CAPTCHA image
# #     location = captcha_img.location
# #     size = captcha_img.size

# #     # Get the screenshot of the entire page
# #     driver.save_screenshot("screenshot.png")

# #     # Crop the CAPTCHA image from the entire screenshot
# #     im = Image.open("screenshot.png")
# #     left = location['x']
# #     top = location['y']
# #     right = location['x'] + size['width']
# #     bottom = location['y'] + size['height']
# #     im = im.crop((left, top, right, bottom))

# #     # Save the cropped image
# #     im.save("captcha.png")

# #     # Preprocess the CAPTCHA image
# #     im = preprocess_image("captcha.png")

# #     # Use pytesseract to do OCR on the preprocessed image
# #     captcha_text = pytesseract.image_to_string(im)

# #     return captcha_text.strip()

# # # Function to fill the form
# # def fill_form(driver, form_data, captcha_input_xpath, captcha_element_xpath):
# #     try:
# #         # Fill the form fields
# #         for field_xpath, value in form_data.items():
# #             form_field = WebDriverWait(driver, 10).until(
# #                 EC.presence_of_element_located((By.XPATH, field_xpath))
# #             )
# #             form_field.send_keys(value)

# #         # Solve CAPTCHA using OCR
# #         captcha_text = solve_captcha(driver, captcha_element_xpath)

# #         # Wait for the CAPTCHA input field to be present
# #         captcha_input = WebDriverWait(driver, 10).until(
# #             EC.presence_of_element_located((By.XPATH, captcha_input_xpath))
# #         )

# #         # Fill the CAPTCHA input field
# #         captcha_input.send_keys(captcha_text)

# #         # Submit the form (assuming there is a submit button with the ID 'submit')
# #         submit_button = driver.find_element(By.XPATH, '//*[@id="submit"]')
# #         submit_button.click()

# #     except Exception as e:
# #         print(f"An error occurred: {e}")
# #     finally:
# #         time.sleep(15)  # Adding a short delay before quitting (you may adjust as needed)
# #         driver.quit()

# # if __name__ == "__main__":
# #     # Replace with your WebDriver path
# #     chromedriver_path = "./chromedriver.exe"

# #     # Configure pytesseract path (you need to install Tesseract OCR)
# #     pytesseract.pytesseract.tesseract_cmd = r'../CAPTURECODE/chromedriver.exe'  # Example path

# #     # Initialize Chrome WebDriver
# #     service = ChromeService(executable_path=chromedriver_path)
# #     options = webdriver.ChromeOptions()
# #     options.add_argument("--ignore-certificate-errors")
# #     options.add_argument("--ignore-ssl-errors")
# #     driver = webdriver.Chrome(service=service, options=options)

# #     try:
# #         # Open the webpage with CAPTCHA
# #         driver.get("https://einvoice1.gst.gov.in/Home/UserRegistration")

# #         # Form data to be filled
# #         form_data = {
# #             '//*[@id="username"]': 'my_username',
# #             '//*[@id="email"]': 'my_email@example.com',
# #             '//*[@id="password"]': 'my_secure_password'
# #         }

# #         # Assuming CAPTCHA input ID is `txtCaptchaCode` (replace if necessary)
# #         captcha_input_xpath = '//*[@id="txtCaptchaCode"]'
# #         captcha_element_xpath = '//*[@id="captcha_image"]'

# #         # Fill the form with the solved CAPTCHA
# #         fill_form(driver, form_data, captcha_input_xpath, captcha_element_xpath)

# #     except Exception as e:
# #         print(f"An error occurred: {e}")
# #     finally:
# #         driver.quit()
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.chrome.service import Service as ChromeService
# # import pytesseract
# # from PIL import Image, ImageEnhance, ImageFilter
# # import time
# # import os

# # # Warning message for ethical considerations
# # print("WARNING: Automating CAPTCHAs often violates website terms and can be unreliable. Consider using a manual solution or contacting the website owner for an alternative method.")

# # # Function to preprocess CAPTCHA image for better OCR accuracy
# # def preprocess_image(image_path):
# #     image = Image.open(image_path)
# #     # Convert to grayscale
# #     image = image.convert('L')
# #     # Apply thresholding to get a binary image
# #     image = image.point(lambda x: 0 if x < 140 else 255, '1')
# #     # Apply some filtering to remove noise
# #     image = image.filter(ImageFilter.MedianFilter())
# #     return image

# # # Function to solve CAPTCHA using OCR
# # def solve_captcha(driver, captcha_element_xpath):
# #     try:
# #         # Locate the CAPTCHA image element
# #         captcha_img = driver.find_element(By.XPATH, captcha_element_xpath)

# #         # Debug: Check if the element is found
# #         print(f"Captcha image element found: {captcha_img.is_displayed()}")

# #         # Get the location and size of the CAPTCHA image
# #         location = captcha_img.location
# #         size = captcha_img.size

# #         # Debug: Print location and size
# #         print(f"Captcha location: {location}, size: {size}")

# #         # Get the screenshot of the entire page
# #         driver.save_screenshot("screenshot.png")

# #         # Crop the CAPTCHA image from the entire screenshot
# #         im = Image.open("screenshot.png")
# #         left = location['x']
# #         top = location['y']
# #         right = location['x'] + size['width']
# #         bottom = location['y'] + size['height']
# #         im = im.crop((left, top, right, bottom))

# #         # Save the cropped image
# #         im.save("captcha.png")

# #         # Debug: Save and show the cropped image
# #         print("Cropped CAPTCHA image saved as 'captcha.png'")

# #         # Preprocess the CAPTCHA image
# #         im = preprocess_image("captcha.png")

# #         # Debug: Save and show the preprocessed image
# #         im.save("preprocessed_captcha.png")
# #         print("Preprocessed CAPTCHA image saved as 'preprocessed_captcha.png'")

# #         # Use pytesseract to do OCR on the preprocessed image
# #         captcha_text = pytesseract.image_to_string(im)

# #         return captcha_text.strip()
# #     except Exception as e:
# #         print(f"An error occurred while solving CAPTCHA: {e}")
# #         return ""

# # # Function to fill the form
# # def fill_form(driver, form_data, captcha_input_xpath, captcha_element_xpath):
# #     try:
# #         # Fill the form fields
# #         for field_xpath, value in form_data.items():
# #             form_field = WebDriverWait(driver, 10).until(
# #                 EC.presence_of_element_located((By.XPATH, field_xpath))
# #             )
# #             form_field.send_keys(value)

# #         # Solve CAPTCHA using OCR
# #         captcha_text = solve_captcha(driver, captcha_element_xpath)
# #         print(f"CAPTCHA text: {captcha_text}")

# #         # Wait for the CAPTCHA input field to be present
# #         captcha_input = WebDriverWait(driver, 10).until(
# #             EC.presence_of_element_located((By.XPATH, captcha_input_xpath))
# #         )

# #         # Fill the CAPTCHA input field
# #         captcha_input.send_keys(captcha_text)

# #         # Submit the form (assuming there is a submit button with the ID 'btnValidate')
# #         submit_button = driver.find_element(By.XPATH, '//*[@id="btnValidate"]')
# #         submit_button.click()

# #     except Exception as e:
# #         print(f"An error occurred: {e}")
# #     finally:
# #         time.sleep(15)  # Adding a short delay before quitting (you may adjust as needed)
# #         driver.quit()

# # if __name__ == "__main__":
# #     # Replace with your WebDriver path
# #     chromedriver_path = "./chromedriver.exe"

# #     # Verify if Tesseract OCR is correctly installed
# #     tesseract_path = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
# #     if not os.path.exists(tesseract_path):
# #         print(f"Tesseract executable not found at {tesseract_path}. Please verify the installation path.")
# #     else:
# #         pytesseract.pytesseract.tesseract_cmd = tesseract_path

# #         # Initialize Chrome WebDriver
# #         service = ChromeService(executable_path=chromedriver_path)
# #         options = webdriver.ChromeOptions()
# #         options.add_argument("--ignore-certificate-errors")
# #         options.add_argument("--ignore-ssl-errors")
# #         driver = webdriver.Chrome(service=service, options=options)

# #         try:
# #             # Open the webpage with CAPTCHA
# #             driver.get("https://einvoice1.gst.gov.in/Home/UserRegistration")

# #             # Form data to be filled
# #             form_data = {
# #                 '//*[@id="txtGstin"]': '27AAACK4289L3Z0'  # Correct XPath for GSTIN input
# #             }

# #             # Assuming CAPTCHA input ID is `txtCaptchaCode` (replace if necessary)
# #             captcha_input_xpath = '//*[@id="txtCaptchaCode"]'
# #             captcha_element_xpath = '//*[@id="captchaImg"]'

# #             # Fill the form with the solved CAPTCHA
# #             fill_form(driver, form_data, captcha_input_xpath, captcha_element_xpath)

# #         except Exception as e:
# #             print(f"An error occurred: {e}")
# #         finally:
# #             driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service as ChromeService
# import pytesseract
# from PIL import Image, ImageEnhance, ImageFilter
# import time
# import os
# import requests
# from io import BytesIO

# # Warning message for ethical considerations
# print("WARNING: Automating CAPTCHAs often violates website terms and can be unreliable. Consider using a manual solution or contacting the website owner for an alternative method.")

# # Function to preprocess CAPTCHA image for better OCR accuracy
# def preprocess_image(image_path):
#     image = Image.open(image_path)
#     # Convert to grayscale
#     image = image.convert('L')
#     # Apply thresholding to get a binary image
#     image = image.point(lambda x: 0 if x < 140 else 255, '1')
#     # Apply some filtering to remove noise
#     image = image.filter(ImageFilter.MedianFilter())
#     return image

# # Function to solve CAPTCHA using OCR
# def solve_captcha(driver, captcha_element_xpath):
#     try:
#         # Locate the CAPTCHA image element
#         captcha_img = driver.find_element(By.XPATH, captcha_element_xpath)

#         # Get the src attribute of the image (URL of the CAPTCHA image)
#         captcha_src = captcha_img.get_attribute('src')

#         # Request the CAPTCHA image from the src URL
#         response = requests.get(captcha_src)
#         captcha_image = Image.open(BytesIO(response.content))

#         # Save the CAPTCHA image (optional for debugging)
#         captcha_image.save("captcha_from_url.png")

#         # Preprocess the CAPTCHA image
#         im = preprocess_image(captcha_image)

#         # Use pytesseract to do OCR on the preprocessed image
#         captcha_text = pytesseract.image_to_string(im)

#         return captcha_text.strip()
#     except Exception as e:
#         print(f"An error occurred while solving CAPTCHA: {e}")
#         return ""

# # Function to fill the form
# def fill_form(driver, form_data, captcha_input_xpath, captcha_element_xpath):
#     try:
#         # Fill the GSTIN field
#         gstin_input_xpath = '//*[@id="txtGstin"]'
#         gstin_input = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, gstin_input_xpath))
#         )
#         gstin_input.send_keys(form_data[gstin_input_xpath])

#         # Solve CAPTCHA using OCR
#         captcha_text = solve_captcha(driver, captcha_element_xpath)
#         print(f"CAPTCHA text: {captcha_text}")

#         # Wait for the CAPTCHA input field to be present
#         captcha_input = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, captcha_input_xpath))
#         )

#         # Fill the CAPTCHA input field
#         captcha_input.send_keys(captcha_text)

#         # Submit the form (assuming there is a submit button with the ID 'btnValidate')
#         submit_button = driver.find_element(By.XPATH, '//*[@id="btnValidate"]')
#         submit_button.click()

#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         time.sleep(5)  # Adding a short delay before quitting (you may adjust as needed)
#         driver.quit()

# if __name__ == "__main__":
#     # Replace with your WebDriver path
#     chromedriver_path = "./chromedriver.exe"

#     # Verify if Tesseract OCR is correctly installed
#     tesseract_path = r'../CAPTURECODE/tesseract.exe'
#     if not os.path.exists(tesseract_path):
#         print(f"Tesseract executable not found at {tesseract_path}. Please verify the installation path.")
#     else:
#         pytesseract.pytesseract.tesseract_cmd = tesseract_path

#         # Initialize Chrome WebDriver
#         service = ChromeService(executable_path=chromedriver_path)
#         options = webdriver.ChromeOptions()
#         options.add_argument("--ignore-certificate-errors")
#         options.add_argument("--ignore-ssl-errors")
#         driver = webdriver.Chrome(service=service, options=options)

#         try:
#             # Open the webpage with CAPTCHA
#             driver.get("https://einvoice1.gst.gov.in/Home/UserRegistration")

#             # Form data to be filled
#             form_data = {
#                 '//*[@id="txtGstin"]': '27AAACK4289L3Z0'  # Correct XPath for GSTIN input
#             }

#             # Assuming CAPTCHA input ID is `txtCaptchaCode` (replace if necessary)
#             captcha_input_xpath = '//*[@id="txtCaptchaCode"]'
#             captcha_element_xpath = '/html/body/div[2]/div[3]/div/div[2]/form[1]/div[2]/div/img'

#             # Fill the form with the solved CAPTCHA
#             fill_form(driver, form_data, captcha_input_xpath, captcha_element_xpath)

#         except Exception as e:
#             print(f"An error occurred: {e}")
#         finally:
# #             driver.quit()
# import requests
import requests
from PIL import Image
import pytesseract
from io import BytesIO

# URL of the CAPTCHA image
captcha_url = 'https://example.com/captcha.png'  # Replace with the actual CAPTCHA image URL

# Download the CAPTCHA image
response = requests.get(captcha_url)
if response.status_code == 200:
    captcha_image = Image.open(BytesIO(response.content))

    # Save the image locally if needed
    captcha_image.save('captcha.png')

    # Use Tesseract to extract text from the image
    captcha_text = pytesseract.image_to_string(captcha_image)

    print("Extracted CAPTCHA text:", captcha_text)
else:
    print("Failed to download CAPTCHA image")
