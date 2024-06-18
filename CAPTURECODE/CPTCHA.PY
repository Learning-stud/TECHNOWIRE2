import asyncio
from pyppeteer import launch
import pytesseract
from PIL import Image
import io

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/CAPTURECODE/tesseract.exe'

async def main():
    try:
        # Launch the browser (use default Chromium)
        browser = await launch(headless=False)  # Removed executablePath to use default Chromium
        page = await browser.newPage()

        # Navigate to the website
        print("Navigating to the website...")
        response = await page.goto('https://gem.gov.in/view_contracts', {'waitUntil': 'networkidle2'})
        print(f"Response status: {response.status}")

        # Check the current URL to confirm navigation
        current_url = page.url
        print(f"Current URL: {current_url}")

        # Capture a screenshot to verify the page content
        await page.screenshot({'path': 'screenshot.png'})
        print("Screenshot taken. Check screenshot.png in your directory.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        await browser.close()

# Run the main function
asyncio.get_event_loop().run_until_complete(main())
