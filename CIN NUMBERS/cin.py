import pandas as pd
import requests
from bs4 import BeautifulSoup

# Load Excel data into a DataFrame
excel_file = '24K.xlsx'  # Replace with your file path
df = pd.read_excel(excel_file)

# Function to extract CIN number from company name
def get_cin_number(Firm_Name):
    search_query = Firm_Name + " CIN number"  # Modify search query if needed
    url = 'https://www.google.com/search?q=' + '+'.join(search_query.split())
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extracting CIN number from Google search results (assuming it's in the first snippet)
    cin_number = soup.find('span', {'class': 'BNeawe'}).text
    return cin_number

# Apply function to each company name in the DataFrame
df['CIN Number'] = df['Firm_Name'].apply(get_cin_number)

# Save updated DataFrame to a new Excel file
output_file = 'company_data_with_cin.xlsx'
df.to_excel(output_file, index=False)

print("CIN numbers extracted and saved to:", output_file)
