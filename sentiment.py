import re
import tweepy 
import pandas as pd
import numpy as np
from tweepy import OAuthHandler
from textblob import TextBlob 
from secrets import *

class TwitterSentiment():
    
    #Tweet Query
    query = "Lockdown"

    #Tweet Count
    count = 40

    #Authorisation
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
    except:
        print("Error: Authentication Failed")

    #Get Tweets
    def get_tweets(self):
        fetched_tweets = self.api.search(q = self.query, count = self.count, lang="en")
        return fetched_tweets

    #Clean the tweets by removing special characters and links
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    
    #Classify sentiment of tweet using TextBlob
    def tweet_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'

    #Create Pandas dataframe to store tweets and sentiment
    def create_data_frame(self, tweets):
        df = pd.DataFrame()
        df['Tweets'] = np.array([tweet.text for tweet in tweets])
        return df
        

if __name__ == "__main__":
    ts = TwitterSentiment()
    tweets = ts.get_tweets()
    ts.create_data_frame(tweets)
    df = ts.create_data_frame(tweets)
    df['Sentiment'] = np.array([ts.tweet_sentiment(tweet) for tweet in df['Tweets']])
    print(df.head(ts.count))