
# import requests
# import pandas as pandu
# from bs4 import BeautifulSoup

# url = "https://www.investing.com/holiday-calendar/"

# # sending the get request to the url and retrive the data/ content
# response = requests.get(url)
# output = BeautifulSoup(response.content,'html.parser')

# # finding  the table containing the holiday data

# table_data = output.find('table',{'id':'holidayCalanderData'})

# # extracting the data
# data = []
# coloums = []

# for row in Table.find_all('tr'):
#  cells = row.find_all(['th','td'])


#  if len(cells)> 0:

#   if not coloums:
#    coloums=[cell.text.strip() for cell in cells]

#   else:
#    data.append([cell.text.strip() for cell in cells])

# # Create a dataframe from the extracted data
# data_form = pandu.DataFrame(data, coloums=coloums)

# # Saving it to the excel file
# excel_file = "holiday_calander.xlsx"
# pandu.to_excel(excel_file, index = False )

# print("Data Saved To => ",excel_file)

# import requests
# import pandas as pd
# from bs4 import BeautifulSoup

# url = "https://www.investing.com/holiday-calendar/"

# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")

# # Find the table containing the holiday data
# table = soup.find("table", {"id": "holidayCalendarData"})

# # Extract data from the table
# data = []
# columns = []
# for row in table.find_all("tr"):
#     cells = row.find_all(["th", "td"])
#     if len(cells) > 0:
#         if not columns:
#             columns = [cell.text.strip() for cell in cells]
#         else:
#             data.append([cell.text.strip() for cell in cells])

# # Create a DataFrame from the extracted data
# df = pd.DataFrame(data, columns=columns)

# # Save the DataFrame to an Excel file
# excel_file = "holiday_calendar.xlsx"
# df.to_excel(excel_file, index=False)

# print("Data saved to", excel_file)
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Define the URL of the webpage
url = "https://www.investing.com/holiday-calendar/"

# Sending a GET request to the URL and retrieve the webpage content
response = requests.get(url)

# Parse the HTML content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the holiday data by its id attribute
holiday_table = soup.find("table", {"id": "holidayCalendarData"})

# Extract data from the table
data = []
for row in holiday_table.find_all("tr"):
    data.append([cell.text.strip() for cell in row.find_all(["th", "td"])])

# Create a DataFrame from the extracted data
holiday_df = pd.DataFrame(data[1:], columns=data[0])

# Save the DataFrame to an Excel file
excel_file = "holiday_calendar.xlsx"
holiday_df.to_excel(excel_file, index=False)

print("Data saved to", excel_file)

