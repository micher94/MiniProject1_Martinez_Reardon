import os
from NPL_module import avg_sentiment
from Twitter_Updated import readtweets
import os
import tweepy as tw

#keys from Twitter API

consumer_key = 'kf4P8Edo8ZXtvgZU8RsmsqY1L'
consumer_secret = '3nyDtxBbeXrJLxo9u5fC8yXbkSySxJTGTSEz26tDc06nAWSm6s'

PATH = input("What is the path for the authentication key: ")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = PATH

text = input("Enter search term here: ")
tweetlist = readtweets(text, consumer_key, consumer_secret)
answer = avg_sentiment(*tweetlist)
print(answer)
