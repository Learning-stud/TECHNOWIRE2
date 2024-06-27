from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://inc42.com/tag/funding-galore/"


driver = webdriver.Chrome()


driver.get(url)


links = []

try:
    while True:

        buttons = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='load-more-feed']")))

        driver.execute_script("arguments[0].click();", buttons)


        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='main']/div/div/div[1]/h2/a")))


        elements = driver.find_elements(By.XPATH, "//*[@id='main']/div/div/div[1]/h2/a")
        for element in elements:
            link = element.get_attribute("href")
            links.append(link)


        buttons = driver.find_elements(By.XPATH, "//*[@id='load-more-feed']")
        if not buttons:
            break

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()

for index, link in enumerate(links, start=1):
    print(f"Link {index}: {link}")
