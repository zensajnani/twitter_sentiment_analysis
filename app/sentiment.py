import re
import tweepy 
import pandas as pd
import numpy as np
from tweepy import OAuthHandler
from textblob import TextBlob 
from .secrets import *

class TwitterSentiment():
    
    #Tweet Query
    # query = input("Query term: ")

    #Tweet Count
    # count = int(input("Number of tweets to be displayed: "))

    def __init__(self, query, count):
        self.query = query
        self.count = int(count)

    #Initialise Count
    positive_count = 0
    negative_count = 0
    neutral_count = 0


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
            self.positive_count += 1
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            self.neutral_count += 1
            return 'neutral'
        else: 
            self.negative_count += 1
            return 'negative'

    #Create Pandas dataframe to store tweets and sentiment
    def create_data_frame(self, tweets):
        df = pd.DataFrame()
        df['Tweets'] = np.array([tweet.text for tweet in tweets])
        return df
        
    def calculate_percentage(self, tweets):
        # Count can not be more than 100
        self.count = 100 if self.count > 100 else self.count 
        positive_percent = (self.positive_count / self.count) * 100
        negative_percent = (self.negative_count / self.count) * 100
        neutral_percent = (self.neutral_count / self.count) * 100
        print(f"\nPositive Tweets: {positive_percent}%")
        print(f"Negative Tweets: {negative_percent}%")
        print(f"Neutral Tweets: {neutral_percent}%\n")
        return {
            'positive_percent': positive_percent,
            'negative_percent': negative_percent,
            'neutral_percent': neutral_percent,
        }
        

# if __name__ == "__main__":
#     ts = TwitterSentiment()
#     tweets = ts.get_tweets()
#     df = ts.create_data_frame(tweets)
#     df['Sentiment'] = np.array([ts.tweet_sentiment(tweet) for tweet in df['Tweets']])
#     print(df.head(ts.count))
#     ts.calculate_percentage(df['Tweets'])
