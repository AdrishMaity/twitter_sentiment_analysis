# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 19:39:53 2018

@author: adrish
"""

import tweepy
import textblob as tb
import csv
import os

consumer_key = '<<your consumer key>>'
consumer_secret_key = '<<your consumer secret key>>'

access_token = '<<your access token>>'
access_token_secret = '<<your access token secret>>'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Sample Search
#searchTerms = 'JOB AND (Datascience OR Python OR Data Science)'
searchTerms = input("What topic you want to find ? : ")

tweets = api.search(q=searchTerms, since='2017-01-01', lang = 'en', count=100)

#Opening the dataset.csv filefor writinh the tweets in it
_path = '<<your path to the save file>'
with open(os.path.join(_path,'twitter_sentiment.out'), mode='w') as tweets_file:
    tweet_writer = csv.writer(tweets_file, delimiter = '|', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    #Labelling the columns for the tweet dataset
    tweet_writer.writerow(['Tweet', 'Author', 'Date', 'Sentiment Polarity'])
    #Analyzing each tweet from the tweets list and storing it in a csv file
    for tweet in tweets:
        tweet_text = tweet.text
        tweet_user = tweet.user.name
        tweet_created_at = tweet.created_at
        tweet_sentiment = tb.TextBlob(tweet_text).sentiment.polarity
        print(tweet_text, tweet_user, tweet_created_at)
        print("Sentiment is %f" % tweet_sentiment)
        try:
            tweet_writer.writerow([tweet_text, tweet_user, tweet_created_at, tweet_sentiment])
        except UnicodeEncodeError:
            pass