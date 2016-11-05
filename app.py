from flask import Flask, render_template, request, json

from flaskext.mysql import MySQL
from process import wordscount
from process import getallpokenames
import time
from threading import Thread

app = Flask(__name__,static_url_path = "")
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ',26187108hoog'
app.config['MYSQL_DATABASE_DB'] = 'pokemon'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

def updateData():
	aa = wordscount()
	pokemonNames = getallpokenames() 

	for name in pokemonNames:
		query = 'UPDATE pokemonCount SET Freq = ' + str(aa[name.lower()]) + ' WHERE Name="' +name+'"'
		cursor.execute(query)
		conn.commit()


def test():
	while(True):
		time.sleep(30)  #  update every one hour(3600s)
		updateData()
		print("----test----")

#Thread(target = test).start()

@app.route('/fight')
def fight():
	return render_template('fight.html')

@app.route("/dictionary")
def dictioinary():
	return render_template('index.html')

@app.route('/twitter')
def show_poke():
	query = "SELECT * FROM pokemonCount ORDER BY Freq DESC LIMIT 4"
	cursor.execute(query)
    	poke = cursor.fetchall()
    	return render_template('twitter.html', poke=poke)

@app.route("/")
def main():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(host='10.0.2.15')   # BUG! BUG! BUG! cannot use ctrl+C to stop it!!!!!
	
	


