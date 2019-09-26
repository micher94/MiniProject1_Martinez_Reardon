# -*- coding: utf-8 -*-
"""
Spyder Editor


"""
import os
import tweepy as tw

def readtweets(searchterm, searchtype, consumer_key, consumer_secret):
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    if searchtype == 1:
        termlength=len(searchterm)
        tweetlist=[]
        if searchterm[0] == '@':
            sn=searchterm[1:termlength]
                   
            for tweets in api.user_timeline(screen_name=sn, result_type = 'recent', tweet_mode = 'extended', count = 200):
                tweetlist.append(tweets.full_text)
        else:
# used https://stackoverflow.com/questions/14856526/parsing-twitter-json-object-in-python to figure out how to pull ONLY the text from the file
# leveraged https://stackoverflow.com/questions/38872195/tweepy-exclude-retweets for how to exclude retweets from twitter list and eliminate duplicates
            for tweets in api.search(q=searchterm, lang = 'en', result_type = 'recent', count = 180):
                if not tweets.retweeted and 'RT @' not in tweets.text:
                    tweetlist.append(tweets.text) 
    else:
        termlength=len(searchterm)
        tweetlist=[]
        if searchterm[0] == '@':
            sn=searchterm[1:termlength]
                   
            for tweets in api.user_timeline(screen_name=sn, result_type = 'popular', tweet_mode = 'extended', count = 5):
                tweetlist.append(tweets.full_text)
            print(tweetlist)
        else:
# used https://stackoverflow.com/questions/14856526/parsing-twitter-json-object-in-python to figure out how to pull ONLY the text from the file
# leveraged https://stackoverflow.com/questions/38872195/tweepy-exclude-retweets for how to exclude retweets from twitter list and eliminate duplicates
            for tweets in api.search(q=searchterm, lang = 'en', result_type = 'popular', count = 5):
                if not tweets.retweeted and 'RT @' not in tweets.text:
                    tweetlist.append(tweets.text)
    #print(fulltweetlist)
    return tweetlist
    
