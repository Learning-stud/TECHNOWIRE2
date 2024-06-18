import asyncio
from pyppeteer import launch
import pytesseract
from PIL import Image
import io
import os

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/CAPTURECODE/tesseract.exe'

async def main():
    # Launch the browser
    browser = await launch(headless=False)  # Set headless=True for a headless browser
    page = await browser.newPage()

    # Navigate to the website
    await page.goto('https://gem.gov.in/view_contracts')

    # Wait for the specific tab to be available and click it
    await page.waitForSelector('#myTab > li:nth-child(2) > a')
    await page.click('#myTab > li:nth-child(2) > a')

    # Wait for the form to load
    await page.waitForSelector('#skip_main_content > div:nth-child(1) > div > div:nth-child(1)')

    # Select the dropdown and input the value
    await page.click('#select2-buyer_ministry-results')
    await page.type('#bodyId > span > span > span > input', 'Central Government')
    await page.keyboard.press('Enter')

    # Handle CAPTCHA
    captcha_element = await page.waitForSelector('#frm > div > div:nth-child(5) > div:nth-child(1) > div:nth-child(3) > div > img')
    captcha_src = await page.evaluate('(captcha_element) => captcha_element.src', captcha_element)

    # Download CAPTCHA image
    captcha_response = await page.goto(captcha_src)
    captcha_image = Image.open(io.BytesIO(await captcha_response.buffer()))
    captcha_text = pytesseract.image_to_string(captcha_image).strip()

    # Input CAPTCHA
    await page.type('#captcha_code2', captcha_text)

    # Click the search button
    await page.click('#searchlocation')

    # Wait for the results to load
    await page.waitForSelector('#pagi_content > div:nth-child(2)')

    # Extract the results
    results = await page.evaluate('document.querySelector("#pagi_content > div:nth-child(2)").innerText')

    print(results)

    # Close the browser
    await browser.close()

# Run the main function
asyncio.get_event_loop().run_until_complete(main())
