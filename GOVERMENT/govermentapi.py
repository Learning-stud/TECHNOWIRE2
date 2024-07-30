import asyncio
from pyppeteer import launch
import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = r'/CAPTURECODE/tesseract.exe'

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()

    await page.goto('https://gem.gov.in/view_contracts')

    await page.waitForSelector('#myTab > li:nth-child(2) > a')
    await page.click('#myTab > li:nth-child(2) > a')

    await page.waitForSelector('#skip_main_content > div:nth-child(1) > div > div:nth-child(1)')

    await page.click('#select2-buyer_ministry-results')
    await page.type('#bodyId > span > span > span > input', 'Central Government')
    await page.keyboard.press('Enter')

    captcha_element = await page.waitForSelector('#frm > div > div:nth-child(5) > div:nth-child(1) > div:nth-child(3) > div > img')
    captcha_src = await page.evaluate('(captcha_element) => captcha_element.src', captcha_element)

    captcha_response = await page.goto(captcha_src)
    captcha_image = Image.open(io.BytesIO(await captcha_response.buffer()))
    captcha_text = pytesseract.image_to_string(captcha_image).strip()

    await page.type('#captcha_code2', captcha_text)

    await page.click('#searchlocation')

    await page.waitForSelector('#pagi_content > div:nth-child(2)')

    results = await page.evaluate('document.querySelector("#pagi_content > div:nth-child(2)").innerText')

    print(results)

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
