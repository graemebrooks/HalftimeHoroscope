import requests
from bs4 import BeautifulSoup

ariesURL = "https://www.astrology.com/horoscope/daily/aries.html"
ariesPage = requests.get(ariesURL)

soup = BeautifulSoup(ariesPage.content, 'html.parser')

results = soup.find(class_='horoscope-main')
horoscope_text = results.find_all('p')

print(horoscope_text[0].text)