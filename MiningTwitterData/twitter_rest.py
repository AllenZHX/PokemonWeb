import tweepy
import json
consumer_key = 'ogNwOOGu41jMxFe96vqqAPsDf'
consumer_secret = 'NH9H7K55SBgQiAOGMyRhvs6dRyoqyhgHIfcok7RhGSNbbEJcp4'
access_token = '3364874174-QMURekZe0QWtSjHdeFRmKkZETdoiMWDltSi0alo'
access_secret = '2LvAcIJ9Z6dbpeArhQ2rqqO9BBfuPSJarTLQg1OvAtNtK'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search,q="Mewtwo",lang="en").items(100):
    print tweet.created_at, tweet.text,tweet.retweet_count
    print tweet.favorite_count
# def process_or_store(tweet):
#     print(json.dumps(tweet))
#
# print "home_timeline:"
# for status in tweepy.Cursor(api.home_timeline).items(5):
#     # Process a single status
#     # process_or_store(status.text)
#     print status.text
#
# print "friends:"
# for friend in tweepy.Cursor(api.friends).items(5):
#     # process_or_store(friend._json)
#     print friend._json
#
# print "user_timeline:"
# for tweet in tweepy.Cursor(api.user_timeline).items(5):
#     process_or_store(tweet._json)
