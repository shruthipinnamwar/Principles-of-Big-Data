#! /usr/bin/env python3

# adapted from simplified web scraping tutorial 
# https://drive.google.com/file/d/0Bw1LIIbSl0xuZ1o4OEtGQlZWdHc/view

import tweepy
import json
import time
from tweepy import OAuthHandler

# authentication info
consumer_key = 'QIsDHEiblIYO2WIFlwDdMYH4n'
consumer_secret = 'BUqsJqomgrPpgaiBRChiLYvfFkGcoGFuUEL8SQPFnAK98ogrX6'
access_token = '906263764940406784-7srNC9pRb7Wz1zHZWqGFMevJ0Nt5Cs3'
access_secret = 'vyF2cQfccQGZtpav843GPhZSMiuiiwuBZtI32KwjCe9BH'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# create API object to automatically wait on Twitter's rate limit
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search_term = 'Olympic'

# do a search for our search term
tweets = tweepy.Cursor(api.search, q=search_term).items()

# loop over each result -- api will pause automatically when we hit rate limit,
# stop and wait for the ban to be lifted, then keep going
count = 0 
error_count = 0
tweets_to_get = 100000

# for fun, let's keep both JSON and regular text of tweets
json_file = open('tweets.json', 'w')
text_file = open('tweets.txt', 'w')

while count <= tweets_to_get: 
        count += 1

        if count % 1000 == 0:
                print(f"{count} tweets retrieved...")

        tweet = next(tweets)

        # uncomment for development without hitting rate limit
        #if count > 10:
        #        break
        try:
                json.dump(tweet._json, json_file, sort_keys=True, indent=4)
                text_file.write(tweet.text + "\n")
                
        except UnicodeEncodeError:
                error_count += 1
                print("UnicodeEncodeError, error_count = " + str(error_count))

json_file.close()
text_file.close()

print("Done")
