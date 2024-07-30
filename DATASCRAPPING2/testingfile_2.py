
import requests
from bs4 import BeautifulSoup

# Base URL
base_url = "https://www.icra.in/Rating/GetPaginationData?RatingType=CR&RatingCategoryId=5&page={}"

def extract_data(page_number):
    url = base_url.format(page_number)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'id': 'entity_data_table'})
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cells = row.find_all('td')
        data.append([cell.text.strip() for cell in cells])
    return data

all_data = []

for page in range(1, 5):
    print(f"Scraping page {page}")
    all_data.extend(extract_data(page))

for row in all_data:
    print(row)


