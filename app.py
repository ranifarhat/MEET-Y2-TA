from databases import *

import urllib.request
import json
import webbrowser

from flask import Flask, flash, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "VerY_sEcREt_kEy"

apodurl = 'https://api.nasa.gov/planetary/apod?api_key='
moikey = 'rrWCm3jvm4910AimLqgIOmZJgxCXJx2QsczkLdxp'

apodurlobj = urllib.request.urlopen(apodurl + moikey)

apodread = apodurlobj.read()

decodeapod = json.loads(apodread.decode('utf-8'))


@app.route("/")
def home():
	return render_template("space.html")

@app.route("/question")
def qshn():
	return render_template("space-s-ui.html")


@app.route("/joinus", methods=["GET", "POST"])
def login():
	global decodeapod
	if request.method == "GET":
		return render_template("space-s-ui.html")
	else:
		username = request.form["username"]
		mail = request.form["email"]

		for prod in query_all():
			if(mail == prod.email):
				# flash("Email already used, please sign in or use different email")
				return render_template("main.html", n=username, i=decodeapod['url'])


		if mail.find("@") == -1 or mail.find(".") == -1:
			flash("Invalid email")
			return render_template("space-s-ui.html")
		elif len(username) == 0 or username == " ":
			flash("Your username can't be a space, nor empty")
		else:
			add_user(mail, username)
			return render_template("main.html", n=username, i=decodeapod['url'])

@app.route('/about')
def about():
    return render_template('aboutme.html')

@app.route('/POTD')
def pic():
	global decodeapod
	return render_template('main.html',  i=decodeapod['url'])


if __name__ == '__main__':
	app.run(debug=True)