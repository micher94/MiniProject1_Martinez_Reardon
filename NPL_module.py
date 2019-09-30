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

#basic get the sentiment value of a string
def get_sentiment(text):
	client = language.LanguageServiceClient()

	document = types.Document(
    	content=text,
    	type=enums.Document.Type.PLAIN_TEXT)

	sentiment = client.analyze_sentiment(document=document).document_sentiment

	return sentiment.score

#input is a list of strings and the output the average of the sentiment value
def avg_sentiment(*text):
	client = language.LanguageServiceClient()
	sentiment_list = []
	for tex in range(len(text)):
		document = types.Document(
    		content=text[tex],
    		type=enums.Document.Type.PLAIN_TEXT)

		sentiment = client.analyze_sentiment(document=document).document_sentiment
		sentiment_list.append(sentiment.score)
	for a in range(len(sentiment_list)):
		if a == 0:
			value1 = sentiment_list[a]
		else:
			value2 = value1 + sentiment_list[a]
			value1 = value2

	average = value1/len(sentiment_list)
	return average