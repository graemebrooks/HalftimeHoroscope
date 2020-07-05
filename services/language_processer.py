from nltk.tokenize import WordPunctTokenizer
import re
from dotenv import load_dotenv, find_dotenv
import os

# Locates and loads environmental variables
load_dotenv(find_dotenv())

import web_scraper as scraper

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def get_sentiment_score(horoscope):
    client = language.LanguageServiceClient()
    document = types\
               .Document(content=horoscope,
                         type=enums.Document.Type.PLAIN_TEXT)
    sentiment_score = client\
                      .analyze_sentiment(document=document)\
                      .document_sentiment\
                      .score
    return sentiment_score


horoscope = scraper.formatted_horoscope("aquarius")
print(get_sentiment_score(horoscope))
