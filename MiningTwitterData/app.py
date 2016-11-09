from flask import Flask
from pymongo import MongoClient

client = MongoClient()
db = client.twitter_DB
collection = db.twitter_Collection

app = Flask(__name__)

tweets_iterator = collection.find({'text': {'$regex': 'Pikachu'}})
count=0
for tweet in tweets_iterator:
    count=count+1
    print tweet['text'],count
    print

f = open('top3','wb')
f.write(str(count)) # python will convert \n to os.linesep
f.close() # you can omit in most cases as the destructor will call it

# @app.route('/pokemon',methods=['POST','PUT','GET'])
# def getAllPokemon():
#     # tweets_iterator = collection.find({'text': {'$regex': 'Mewtwo'}}).limit(10)
#     tweets_iterator=collection.find().limit(5)
#     # res = ''
#     for tweet in tweets_iterator:
#         print tweet['text']
#         # res = res+tweet['text']
#
#     # return res
#
# if __name__ == '__main__':
#     app.run(debug=True)
