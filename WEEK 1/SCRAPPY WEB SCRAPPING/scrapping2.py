import requests
from bs4 import BeautifulSoup

def scrape_weather(location):
    url = f'https://www.weather.com/weather/today/l/{location}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        temperature = soup.find(class_='CurrentConditions--tempValue--3KcTQ').get_text()
        conditions = soup.find(class_='CurrentConditions--phraseValue--2xXSr').get_text()
        return {'temperature': temperature, 'conditions': conditions}
    else:
        print(f'Error: Failed to fetch weather data for {location}')
        return None

if __name__ == '__main__':
    location = '94105'  # Example: Zip code for San Francisco
    weather_data = scrape_weather(location)
    if weather_data:
        print(f'Temperature: {weather_data["temperature"]}')
        print(f'Conditions: {weather_data["conditions"]}')

