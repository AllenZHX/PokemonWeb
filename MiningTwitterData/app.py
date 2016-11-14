from flask import Flask
from pymongo import MongoClient

client = MongoClient("mongodb://xiang:1@ds149437.mlab.com:49437/twitter_db")
db = client.twitter_db
collection = db.twitter_collection

app = Flask(__name__)

def countTweets(name):
    tweets_iterator = collection.find({'text': {'$regex': name}})
    count = 0
    for tweet in tweets_iterator:
        count = count + 1
        # print tweet['text'], count
        # print   "***********"
    return count

print countTweets("Mewtwo")

# f = open('top3','wb')
# f.write(str(count)) # python will convert \n to os.linesep
# f.close() # you can omit in most cases as the destructor will call it

@app.route('/',methods=['POST','PUT','GET'])
def getAllPokemon():
    res=""
    tweets_iterator = collection.find({'text': {'$regex': 'Pikachu'}}).limit(10)
    # tweets_iterator=collection.find().limit(5)
    for tweet in tweets_iterator:
        # print tweet['text']
        res =res+(tweet['text'])+">>>>>>>>>>>>>>>>"
    return res

if __name__ == '__main__':
    app.run()
