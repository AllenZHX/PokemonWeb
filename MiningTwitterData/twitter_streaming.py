from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

from pymongo import MongoClient
import json

# consumer key, consumer secret, access token, access secret.
ckey =''
csecret = 'NH9H7K'
atoken = '33648KkZETdoiMWDltSi0alo'
asecret = '2LvAcIJ9Z6dbpQg1OvAtNtK'

class listener(StreamListener):
    def on_data(self, data):
        print(data)

        with open('pokemon.json','a') as f:
            f.write(data)

        client = MongoClient()
        db = client.twitter_DB
        collection = db.twitter_Collection
        tweet=json.loads(data)
        collection.insert(tweet)

        return True

    def on_error(self, status):
        print status


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Pokemon"])
