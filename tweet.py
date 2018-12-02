# from tweepy.streaming import StreamListener
# from tweepy import OAuthHandler
# from tweepy import Stream

import tweepy

consumer_key = "rTVQFs0E39iDlT9z2HjtvoypP"
consumer_secret = "i4ne9Z2k9cThWjR0FD2YMotGRT9qJcFUq6axkQHLZRXGfneqOm"
access_token = "316920647-EqVEVvor9VYZ73beLSCXfwUsmGcsjCM9yxxgjnb5"
access_token_secret = "QF41oHaAVHExCKNZxO19fwoBzXcVzdGlpEpIUylFF1P4r"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

count_of_tweets = 10
language = "en"
number_of_tweets = 0

#public_tweets = api.search("hello",lang = language, rpp = 10)
public_tweets = api.search ("food", count = count_of_tweets,lang = language)
for tweet in public_tweets:
    number_of_tweets += 1
    print(tweet.text)

print(number_of_tweets)

# grab user name
