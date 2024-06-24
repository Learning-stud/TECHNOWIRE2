import requests
from bs4 import BeautifulSoup
import csv

# Fetch the webpage
url = 'https://inc42.com/buzz/from-zepto-to-bira-91-indian-startups-raised-800-mn-this-week/'
response = requests.get(url)
html_content = response.content

# Parse HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table
table = soup.find('tbody  ')

# Extract table data and save to CSV
if table:
    with open('startup_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header row
        header_row = [header.get_text(strip=True) for header in table.find_all('th')]
        writer.writerow(header_row)

        # Write data rows
        rows = table.find_all('tr')
        for row in rows[1:]:  # Skip the first row (header row is already written)
            csv_row = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
            writer.writerow(csv_row)

    print('CSV file created successfully.')
else:
    print('No table found on the webpage.')
