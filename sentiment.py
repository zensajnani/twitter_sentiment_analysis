import re
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
from secrets import *

#Authorisation
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
except:
    print("Error: Authentication Failed")



