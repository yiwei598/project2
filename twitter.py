# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#!/usr/bin/env python
# encoding: utf-8
#Author - Prateek Mehta



import tweepy #https://github.com/tweepy/tweepy
import json
import wget

#Twitter API credentials
consumer_key = "enter your own key"
consumer_secret = "enter your own key"
access_key = "enter your own key"
access_secret = "enter your own key"


if __name__ == '__main__':
    #pass in the username of the account you want to download
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)


    search_word = "puppy filter:images -filter:retweets"
    date_since = 2020-9-1
    tweets = tweepy.Cursor(api.search, q=search_word, lang="en", since=date_since).items(3)
    media_files = set()
    media_url = []

    for tweet in tweets:
        print(tweet.text)
        media = tweet.entities.get('images', [])
        media_url.append(media)



