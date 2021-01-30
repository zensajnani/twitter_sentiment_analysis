from app import app
import numpy as np
from flask import Flask, render_template, request
from .sentiment import TwitterSentiment

# app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#API to return all the classified tweets
@app.route('/api/result', methods=['GET', 'POST'])
def result():
    query = request.form['query']
    print(query)
    tweet_count = request.form['tweetCount']


    ts = TwitterSentiment(query, tweet_count)
    tweets = ts.get_tweets()
    df = ts.create_data_frame(tweets)
    df['Sentiment'] = np.array([ts.tweet_sentiment(tweet) for tweet in df['Tweets']])
    print(df.head(ts.count))
    df_dict = df.to_dict()
    print(df_dict)
    percentages = ts.calculate_percentage(df['Tweets'])

    return {'result': df_dict, 'percentages': percentages}

# if __name__ == "__main__":
#     app.run(debug=True)