from bs4 import BeautifulSoup
import requests


Product_name = []
Prices = []
Descriptions =[]
Reviews = []

url = 'https://www.flipkart.com/search?q=mobiles%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

data= requests.get(url)
# print(data)
soup = BeautifulSoup(data.text,'lxml')
# print(soup)
names = soup.find_all('div', class_="KzDlHZ")
# print(names)

for datas in names:
 name=datas.text
 Product_name.append(name)

# print(len(Product_name))

prices = soup.find_all('div', class_="Nx9bqj _4b5DiR")
# print(prices)

for i in prices:
 name=i.text
 prices.append(name)
 print(prices)


# desc = soup.find_all("ul", class_="G4BRas" )
# print(desc)