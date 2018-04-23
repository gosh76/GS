# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 10:52:23 2018 by Goldie Sahni
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

ckey='ArLEwjpvPNXVSqwogd78pRQk6'
csecret='SsgtrMBoLmKNZVxolUPvDAURwxjFrpEzTnzLa5pJzXE3UZR4nV'
atoken='361915224-M7MA7drXwbEY3xDrbGgUT1wDLeEmYmOIamsrMqzc'
asecret='1RH4bOzAFd7cJaOAWavxDApTIKEjaAbBPY6EmPPZOiBkK'

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        
        username = all_data["user"]["screen_name"]
        
        print((username,tweet))
        
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Tesla"])
