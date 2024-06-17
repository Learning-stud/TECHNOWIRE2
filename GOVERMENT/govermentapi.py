import requests
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image
from io import BytesIO
import base64

# Define URLs
initial_url = 'https://gem.gov.in/view_contracts'
session = requests.Session()

# Step 1: Get the initial page
response = session.get(initial_url)
response.raise_for_status()  # Ensure we notice bad responses
soup = BeautifulSoup(response.content, 'html.parser')

# Save the page content to identify the CAPTCHA image
with open("initial_page.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())

print("Initial page saved to 'initial_page.html'. Please open this file to identify the CAPTCHA image URL.")

# Extract CAPTCHA image base64 string
captcha_image_tag = soup.find('img', {'id': 'captchaimg1'})
if captcha_image_tag is None:
    raise ValueError("CAPTCHA image tag not found. Please check the ID or other attributes.")

captcha_image_src = captcha_image_tag['src']
print(f"CAPTCHA Image src attribute: {captcha_image_src}")

# Ensure the src attribute is in the expected base64 format
if not captcha_image_src.startswith('data:image'):
    raise ValueError("CAPTCHA image src attribute is not in the expected format. Please check the src content.")

# Extract base64 part of the src attribute
try:
    captcha_image_base64 = captcha_image_src.split(',')[1]
except IndexError:
    raise ValueError("Failed to split the src attribute. Please check the format of the src content.")

# Decode the base64 string to get the image
captcha_image_data = base64.b64decode(captcha_image_base64)

# Load the image into PIL
captcha_image = Image.open(BytesIO(captcha_image_data))

# Use Pytesseract to read the CAPTCHA
try:
    captcha_text = pytesseract.image_to_string(captcha_image).strip()
    print(f"CAPTCHA text: {captcha_text}")
except Exception as e:
    print("Error in reading the CAPTCHA image:", e)
    raise

# Add the CAPTCHA text to form data
form_data = {
    'buyer_ministry': 'Central Government',
    'captcha_code2': captcha_text  # Adjust name as necessary
}

# Extract the form action URL
form = soup.find('form')
if not form:
    raise ValueError("Form not found on the page. Please check the page structure.")

form_action = form['action']
form_action_url = requests.compat.urljoin(initial_url, form_action)

# Submit the form with the captured data and CAPTCHA
response = session.post(form_action_url, data=form_data)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract and display the data
data_section = soup.find('div', {'id': 'pagi_content'})
if not data_section:
    raise ValueError("Data section not found on the page. Please check the page structure.")

data_items = data_section.find_all('div')  # Adjust the tag and class name as necessary

# Print the extracted data
for item in data_items:
    print(item.text.strip())
