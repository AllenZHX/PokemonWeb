import tweepy
import json
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

print "home_timeline:"
for status in tweepy.Cursor(api.home_timeline).items():
    # Process a single status
    process_or_store(status._json)

print "friends:"
for friend in tweepy.Cursor(api.friends).items(5):
    process_or_store(friend._json)

print "user_timeline:"
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)
