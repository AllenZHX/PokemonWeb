from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

from pymongo import MongoClient
import json

# consumer key, consumer secret, access token, access secret.
ckey ='ogNwOOGu41jMxFe96vqqAPsDf'
csecret = 'NH9H7K55SBgQiAOGMyRhvs6dRyoqyhgHIfcok7RhGSNbbEJcp4'
atoken = '3364874174-QMURekZe0QWtSjHdeFRmKkZETdoiMWDltSi0alo'
asecret = '2LvAcIJ9Z6dbpeArhQ2rqqO9BBfuPSJarTLQg1OvAtNtK'

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
# twitterStream.filter(track=["Pikachu","MewTwo","Bulbasaur"])
twitterStream.filter(track=["Pokemon","Pikachu","MewTwo","Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran","Nidorina","Nidoqueen","Nidoran","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"])
