from flask import Flask, render_template, request, json

from flask.ext.mysql import MySQL
from process import wordscount
from process import getallpokenames
from process import getPokeTwitter
from process import countTweets
import time
from threading import Thread

app = Flask(__name__,static_url_path = "")
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_USER'] = 'flaskdemo'
app.config['MYSQL_DATABASE_PASSWORD'] = ',26187108hoog'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'flaskdemo'
app.config['MYSQL_DATABASE_DB'] = 'pokemon'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#app.config['MYSQL_DATABASE_HOST'] = 'flasktest.cf70m8cjvbfe.us-east-1.rds.amazonaws.com'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

#################################################################################################################
##############################################for real time project##############################################
def updateData():    #use tokenize 											#
	aa = wordscount()											#
	pokemonNames = getallpokenames() 									#
														#
	for name in pokemonNames:										#
		query = 'UPDATE pokemonCount SET Freq = ' + str(aa[name.lower()]) + ' WHERE Name="' +name+'"'   #
		cursor.execute(query)										#
		conn.commit()											#

def updateData02():    #use mongodb
	pokemonNames = getallpokenames() 
	for name in pokemonNames:
		aa = countTweets(name.lower());										#
		query = 'UPDATE pokemonCount SET Freq = ' + str(aa) + ' WHERE Name="' +name+'"'   #
		cursor.execute(query)										#
		conn.commit()
														#
def test():													#
	while(True):												#
		time.sleep(30)  #  update every one hour(3600s)							#
		updateData()											#
		print("----test----")										#
														#
#Thread(target = test).start()											#
#################################################################################################################
#updateData02()
@app.route('/signUp', methods=['POST'])
def signUp():
    try:
	_YourID = request.form['YourID']
	cursor.execute("SELECT Name,Type_1,Type_2 FROM pokemonData WHERE id=%s",_YourID)
	YourInfo = cursor.fetchall()
	_EnemyID = request.form['EnemyID']
	cursor.execute("SELECT Name,Type_1,Type_2 FROM pokemonData WHERE id=%s",_EnemyID)
	EnemyInfo = cursor.fetchall()
	

	return json.dumps({'yourpokename':str(YourInfo[0][0]),'yourpoketype1':str(YourInfo[0][1]),'yourpoketype2':str(YourInfo[0][2]),'enemypokename':str(EnemyInfo[0][0]),'enemypoketype1':str(EnemyInfo[0][1]),'enemypoketype2':str(EnemyInfo[0][2])})
    except Exception as e:
        return json.dumps({'error':str(e)})

@app.route('/signUp02', methods=['POST'])
def signUp02():
    try:
	_YourType1 = request.form['YourType1']
	_EnemyType1 = request.form['EnemyType1']
	cursor.execute("SELECT " + _EnemyType1 + " FROM pokemonRest WHERE Type='" + _YourType1 + "'")
	YourInfo = cursor.fetchall()
	cursor.execute("SELECT " + _YourType1 + " FROM pokemonRest WHERE Type='" + _EnemyType1 + "'")
	EnemyInfo = cursor.fetchall()

	return json.dumps({'yourdamage':str(YourInfo[0][0]),'enemydamage':str(EnemyInfo[0][0])})
    except Exception as e:
        return json.dumps({'error':str(e)})

@app.route('/fight')
def fight():
	return render_template('fight.html')

@app.route("/dictionary")
def dictioinary():
	return render_template('index.html')

@app.route('/twitter')
def show_poke():
	query = "SELECT * FROM pokemonCount ORDER BY Freq DESC LIMIT 151"
	cursor.execute(query)
    	poke = cursor.fetchall()
	twitterdata = getPokeTwitter(poke[0][1].lower())
    	return render_template('twitter.html', poke=poke, twitterdata=twitterdata)

@app.route("/")
def main():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(host='10.0.2.15')   # BUG! BUG! BUG! cannot use ctrl+C to stop it!!!!!
	# app.run()   # BUG! BUG! BUG! cannot use ctrl+C to stop it!!!!!

	


