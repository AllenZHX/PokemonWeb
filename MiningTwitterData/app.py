from flask import Flask
from pymongo import MongoClient

client = MongoClient()
db = client.twitter_DB
collection = db.twitter_Collection

app = Flask(__name__)

@app.route('/pokemon',methods=['POST','PUT','GET'])
def getAllPokemon():
    tweets_iterator = collection.find().limit(10)
    res = ''
    for tweet in tweets_iterator:
        print tweet['text']
        res=res+tweet['text']

    return res

if __name__ == '__main__':
    app.run(debug=True)
