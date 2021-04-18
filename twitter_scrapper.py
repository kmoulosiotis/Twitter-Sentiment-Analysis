import tweepy
import csv
import pandas as pd

# Twitter keys

CONSUMER_KEY = " "
CONSUMER_SECRET = " "
ACCESS_TOKEN = " "
ACCESS_TOKEN_SECRET = " "

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Creating the API object while passing in auth information
api = tweepy.API(auth)

# columns = ['Tweet', 'User', 'Location', 'Timestamp', 'Geocode']
keywords = ['#Afganistan', 'afganistan','afganistan war', '#AfghanPeaceProcess', 'us withdraw']


for k in keywords:
    query = tweepy.Cursor(api.search, q=k, lang='en').items(100)
    tweets = [{'Tweet':tweet.text, 'User':tweet.user.screen_name, 'Location':tweet.user.location,'Likes':tweet.favorite_count, 'Retweets':tweet.retweet_count ,'Timestamp':tweet.created_at, 'Geocode':tweet.geo} for tweet in query]

    df = pd.DataFrame(tweets)

    df.to_csv('Data/afganistan_war.csv', mode='a', header=None)


## Scraping Started at 18/4/2021 