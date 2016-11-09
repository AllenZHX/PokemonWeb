from TwitterSearch import *
import json
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    # tso.set_keywords(['Pokemon','Mewtwo','Pikachu','bulbasaur'])
    tso.set_keywords(['Pokemon','Pikachu'])
    # tso.set_keywords(['Guttenberg', 'Doktorarbeit']) # let's define all words we would like to have a look for
    # tso.set_language('de') # we want to see German tweets only
    # tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key='ogNwOOGu41jMxFe96vqqAPsDf',
        consumer_secret = 'NH9H7K55SBgQiAOGMyRhvs6dRyoqyhgHIfcok7RhGSNbbEJcp4',
        access_token = '3364874174-QMURekZe0QWtSjHdeFRmKkZETdoiMWDltSi0alo',
        access_token_secret = '2LvAcIJ9Z6dbpeArhQ2rqqO9BBfuPSJarTLQg1OvAtNtK'
        # consumer_key = 'aaabbb',
        # consumer_secret = 'cccddd',
        # access_token = '111222',
        # access_token_secret = '333444'
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        # print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        # print (tweet['text'])
        print tweet

        # with open('pokemon.json', 'a') as f:
        #     loadedTweet=json.loads(tweet)
        #     f.write(loadedTweet)

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)