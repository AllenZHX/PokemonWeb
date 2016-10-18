from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route('/head')
def head():
	return render_template('head.html')

@app.route('/foot')
def foot():
	return render_template('foot.html')


@app.route('/fight')
def fight():
	return render_template('fight.html')

@app.route('/twitter')
def twitter():
	return render_template('twitter.html')

@app.route("/dictionary")
def dictioinary():
	return render_template('index.html')

@app.route("/")
def main():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(host="10.0.0.12")
