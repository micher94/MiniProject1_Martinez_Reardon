import os
from NPL_module import what_sentiment

PATH = input("What is the path for the authentication key: ")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = PATH

text = input("Enter text: ")
what_sentiment(text)
