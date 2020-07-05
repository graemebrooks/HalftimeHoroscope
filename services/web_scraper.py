import requests
import get_horoscope_data as scraper
from bs4 import BeautifulSoup

def formatted_horoscope(sign):
    results = scraper.get_data(sign).find(class_='horoscope-main')
    horoscope_text = results.find_all('p')

    return horoscope_text[0].text
    


