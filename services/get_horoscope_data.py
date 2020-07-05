import requests
from bs4 import BeautifulSoup

def get_data(sign):
    URL = "https://www.astrology.com/horoscope/daily/{sign}.html".format(sign=sign)
    page = requests.get(URL)
    parsedPage = BeautifulSoup(page.content, 'html.parser')

    return parsedPage 