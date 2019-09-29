import os
from NPL_module import avg_sentiment
from Twitter_Updated import readtweets
import os
import tweepy as tw

#keys from Twitter API

consumer_key = 'kf4P8Edo8ZXtvgZU8RsmsqY1L'
consumer_secret = '3nyDtxBbeXrJLxo9u5fC8yXbkSySxJTGTSEz26tDc06nAWSm6s'

PATH = "C:\\Users\\martinezg1\\Documents\\BU\\EC601\\Mini-Project 1\\NPL_auth.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = PATH

print("Menu")
print("1. Read Top 5 Tweets")
print("2. What is the sentiment?")

while True:
        choice = input("Press the number to choose what you want to do: ")
        if choice == "1":
                text = input("Enter search term here: ")
                print("Here are the Top 5 tweets for " + text)
                print("")
                t5tweets = readtweets(text,0,consumer_key, consumer_secret)
                for i in range(len(t5tweets)):
                        print(t5tweets[i])
                        print("")
                
        elif choice == "2":
                text = input("Enter search term here: ")
                if(text[0] == "@"):
                        tweetlist = readtweets(text,1,consumer_key, consumer_secret)
                        print("Please Wait...")
                        answer = avg_sentiment(*tweetlist)
                        if (answer >= 0.25 and answer <= 1):
                                print(text + " is positive right now!")
                        elif (answer >= -0.25 and answer < 0.25):
                            print(text + " is neutral right now!")
                        elif (answer >= -1 and answer < -0.25):
                            print(text + " is negative right now!")
                       
                
                elif (text[0] == "#"):
                        tweetlist = readtweets(text,1, consumer_key, consumer_secret)
                        print("Please Wait...")
                        answer = avg_sentiment(*tweetlist)
                        if (answer >= 0.25 and answer <= 1):
                            print(text, "is positive right now!")
                        elif (answer >= -0.25 and answer < 0.25):
                            print(text, "is neutral right now!")
                        elif (answer >= -1 and answer < -0.25):
                            print(text, "is negative right now!")
                        
                else:
                        tweetlist = readtweets(text,1,consumer_key, consumer_secret)
                        print("Please Wait...")
                        answer = avg_sentiment(*tweetlist)
                        if (answer >= 0.25 and answer <= 1):
                            print(text, " is positive right now!")
                        elif (answer >= -0.25 and answer < 0.25):
                            print(text, " is neutral right now!")
                        elif (answer >= -1 and answer < -0.25):
                            print(text, " is negative right now!")
                              
        else:
                print("Please Enter a Valid Choice")

        restart = input("Would you like to restart the program? Type Yes or No: ")
       
        if restart == 'No' or restart == "no":
                break
        if restart == "Yes" or restart == "yes":
                continue

input("Press Enter to continue...")
