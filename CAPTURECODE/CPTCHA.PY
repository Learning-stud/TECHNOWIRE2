import asyncio
from pyppeteer import launch
import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = r'/CAPTURECODE/tesseract.exe'

async def main():
    browser = None
    try:
        browser = await launch(headless=False, executablePath='C:/Program Files/Google/Chrome/Application/chrome.exe')
        page = await browser.newPage()

        print("Navigating to the website...")
        retries = 3
        for attempt in range(retries):
            try:
                await page.goto('https://gem.gov.in/view_contracts', {'waitUntil': 'networkidle2'})
                break
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt == retries - 1:
                    raise
                await asyncio.sleep(2)
        print("Navigated to the website.")

        current_url = page.url
        if current_url == 'about:blank':
            raise Exception("Navigation failed, current URL is about:blank")
        print(f"Current URL: {current_url}")

        await page.screenshot({'path': 'screenshot.png'})
        print("Screenshot taken.")

        await page.waitForSelector('#myTab > li:nth-child(2) > a', timeout=10000)
        await page.click('#myTab > li:nth-child(2) > a')
        print("Clicked on the second tab.")

        await page.waitForSelector('#skip_main_content > div:nth-child(1) > div > div:nth-child(1)', timeout=10000)
        print("Form is loaded.")

        await page.click('#select2-buyer_ministry-results')
        await page.type('#bodyId > span > span > span > input', 'Central Government')
        await page.keyboard.press('Enter')
        print("Dropdown value selected.")

        captcha_element = await page.waitForSelector('#frm > div > div:nth-child(5) > div:nth-child(1) > div:nth-child(3) > div > img', timeout=10000)
        captcha = await page.evaluate('(captcha_element) => captcha_element.src', captcha_element)
        print("Captcha image source retrieved.")

        response = await page.goto(captcha)
        image = Image.open(io.BytesIO(await response.buffer()))
        text_captcha = pytesseract.image_to_string(image).strip()
        print("Captcha text extracted:", text_captcha)

        await page.type('#captcha_code2', text_captcha)
        print("Captcha text inputted.")

        await page.click('#searchlocation')
        print("Search button clicked.")

        await page.waitForSelector('#pagi_content > div:nth-child(2)', timeout=10000)
        print("Results are loaded.")

        results = await page.evaluate('document.querySelector("#pagi_content > div:nth-child(2)").innerText')
        print("Results extracted.")

        print(results)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if browser:
            await browser.close()

asyncio.get_event_loop().run_until_complete(main())
