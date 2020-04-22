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


class TwitterSentiment(object):

    def timeline_tweets(self):
        public_tweets = api.home_timeline()
        for tweet in public_tweets:
            print(tweet.text)

    def twitter_user(self):
        user = api.get_user('Zen_Sajnani')
        print(user)

    def search_hashtag(self, hashtag):
        number_of_tweets = 5
        for tweet in tweepy.Cursor(api.search,q="#{}".format(hashtag), lang="en").items(number_of_tweets):
            if tweet.retweeted:
                print("Retweeted")
                number_of_tweets += 1
            else:
                print("Not Retweeted")
                print (tweet.text)

ts = TwitterSentiment()

