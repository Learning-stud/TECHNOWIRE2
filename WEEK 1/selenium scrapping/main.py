# Selenium
# pip install selenium
# pip install webdriver-manager

# import time
# import pandas as pd
# # web driver for  automating web browser interaction
# from selenium import webdriver
# # service from selinium toi configure the browser service
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# #  for managing chrome driver
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# # navigates to the specifc url
# driver.get('https://www.investing.com/holiday-calendar/')


# # locating the table data with the id  on the web page
# table_element = driver.find_element(By.ID, 'holidayCalendarData')


# #  finding all coloumns headers within the table headers using xpath
# columns = table_element.find_elements(By.XPATH, '//*[@id="holidayCalendarData"]/thead[1]/tr/th')


# #  finding all rows
# rows =  table_element.find_elements(By.TAG_NAME,'tr')


# #  extracting the text from each coloumn header elements and storing in coloumn_data variable
# columns_data = [i.text for i in columns]


# #  iterations of cells data and extracting their text content  and adding it to data_list variable
# row_data = []
# for row in rows:
#     cells = row.find_elements(By.TAG_NAME,'td')
#     data = [cell.text.strip() for cell in cells]
#     if data:
#         row_data.append(data)

# #  debugging
# # print("Columns:",columns_data)
# # print("Rows:",row_data)

# # creating data frame from the collected data with coloumn header specific
# df = pd.DataFrame(row_data, columns=columns_data)

# #  saving it to the excel file
# excel_file = "holiday_calendar.xlsx"
# df.to_excel(excel_file, index=False)


# driver.quit()


# Selenium
# pip install selenium
# pip install webdriver-manager

# import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.investing.com/holiday-calendar/')

table_element = driver.find_element(By.CLASS, 'CTPDataTable')

columns = table_element.find_elements(By.XPATH, '//*[@id="holidayCalendarData"]/thead[1]/tr/th')
rows =  table_element.find_elements(By.TAG_NAME,'tr')

columns_data = [i.text for i in columns]
row_data = []

for row in rows:
    cells = row.find_elements(By.TAG_NAME,'td')
    data = [cell.text.strip() for cell in cells]
    if data:
        row_data.append(data)

# print("Columns:",columns_data)
# print("Rows:",row_data)



df = pd.DataFrame(row_data, columns=columns_data)
# print(df)

# Save the DataFrame to an Excel file
excel_file = "holiday_calendar.xlsx"
df.to_excel(excel_file, index=False)

print("Data saved to", excel_file)

driver.quit()