import schedule
import tweepy
from dotenv import load_dotenv, find_dotenv
import os

# Locates and loads environmental variables
load_dotenv(find_dotenv())

# Authenticate to Twitter
API_KEY = os.environ.get("API_KEY")
API_SECRET_KEY = os.environ.get("API_SECRET_KEY")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# -----------------Schedule python functions-----------------
# def job():  
#     print("A Simple Python Scheduler.")  

# run the function job() every 2 seconds  
# schedule.every(2).seconds.do(job)  

# while True:  
#     schedule.run_pending()  
