# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 15:29:28 2018 by Goldie Sahni
"""
import numpy as np
import pandas as pd
import csv


import tweepy
ckey='ArLEwjpvPNXVSqwogd78pRQk6'
csecret='SsgtrMBoLmKNZVxolUPvDAURwxjFrpEzTnzLa5pJzXE3UZR4nV'
atoken='361915224-M7MA7drXwbEY3xDrbGgUT1wDLeEmYmOIamsrMqzc'
asecret='1RH4bOzAFd7cJaOAWavxDApTIKEjaAbBPY6EmPPZOiBkK'


auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

api = tweepy.API(auth)

query = '@paytm'
max_tweets = 2000
searched_tweets = [status.text for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

len(searched_tweets)
searched_tweets[0]

s1 = pd.DataFrame(searched_tweets,columns=['tweet'])
s1.to_csv('F:/TWEETS.csv',index=False)


