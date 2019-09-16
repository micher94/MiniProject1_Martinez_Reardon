import os
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def what_sentiment(text):
#set environmental variable to point to authentication json key
#"C:\\Users\\martinezg1\\Documents\\New folder\\auth.json"
    
	client = language.LanguageServiceClient()

# The text to analyze
	document = types.Document(
    	content=text,
    	type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
	sentiment = client.analyze_sentiment(document=document).document_sentiment
	if sentiment.score >= 0.5 and sentiment.score <= 1:
		print("You are having a good day")
	if sentiment.score <= 0:
		print("Today is a bad day")
	if sentiment.score > 0 and sentiment.score <0.5:
		print("Neutral")
	#print('Text: {}'.format(text))
	print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
PATH = input("What is the path for the authentication key: ")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = PATH
text = input("Enter text to be analyzed: ")
what_sentiment(text)
