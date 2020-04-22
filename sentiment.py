import re
import tweepy 
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
from textblob import TextBlob 
from secrets import *

#Authorisation
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
except:
    print("Error: Authentication Failed")



class Listener(StreamListener):
    def on_data(self, data):
        print(data)
        return True
    
    def on_error(self, status):
        print(status)

twitterStream = Stream(auth, Listener())
twitterStream.filter(track=["Lockdown"])