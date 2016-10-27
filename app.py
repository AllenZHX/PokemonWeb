from flask import Flask, render_template, request, json

from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ',26187108hoog'
app.config['MYSQL_DATABASE_DB'] = 'pokemon'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/fight')
def fight():
	return render_template('fight.html')

@app.route("/dictionary")
def dictioinary():
	return render_template('index.html')

@app.route('/twitter')
def show_poke():
	conn = mysql.connect()
	cursor = conn.cursor()
	query = "SELECT * FROM pokemonData WHERE Legendary='true'"
	cursor.execute(query);
    	poke = cursor.fetchall()
    	return render_template('twitter.html', poke=poke)

@app.route("/")
def main():
	return render_template('index.html')

if __name__ == "__main__":
	app.run()
