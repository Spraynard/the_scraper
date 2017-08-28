from flask import Flask
from flask import render_template

import sqlite3
conn = sqlite3.connect('db/test_server.db')

app = Flask(__name__, static_url_path="/static")
app.secret_key = '3\xb9\xff\xa9\xef\x14\xe3d\x93\x19\x02]\xa2\xb1\xad\xd4\xbe> \xf5\xc5\xbc\x1a6'

@app.route("/")
def hello():
	string = "Hello World!"
	return render_template('home.html', message=string)


@app.route("/test-1")
	# This will be a listing of doctors and names.
	# 	Need to obtain this specific data through
	#	scraping. Looking to have a CSV of the values.
def test_1():
	c = conn.cursor()
	c.execute('SELECT * FROM doctors')
	
	doctors = c.fetchall()

	return render_template('test-1.html', doctors=doctors)

@app.route("/test-2")
# Test 2 - Five Pictures on the screen.
#			testing whether the scraper will be downloading
#			all five pictures.
def test_2():
	return render_template('test-2.html')

@app.route("/test-3")
def test_3_home():
	return render_template('test-3-main.html')

@app.route("/test-3/<link_number>")
# Test 3 - Tests the crawling abilities of the scraper
#			Will set up a page with links and ask that the crawler
#			go through all those links and download all pages the
#			links go to. 
def test_3(link_number):
	return render_template('test-3-main.html', link_number=link_number)

@app.route("/test-4", methods=['GET', 'POST'])
# Test 4 - Authentication Test. Used to test feeding
#			the scraper auth values and then seeing
# 			if it can get past an auth wall.
def test_4():
	from flask import request, session, redirect, url_for
	if request.method == 'POST':
		user_dict = {}
		c = conn.cursor()
		c.execute("SELECT * FROM users")
		for user in c.fetchall():
			user_dict[user[0]] = user[1]
		un_input = request.form['username']
		pw_input = request.form['password']
		if un_input in user_dict.keys() and pw_input in user_dict.values():
			session['username'] = un_input
			return redirect(url_for('hello'))
	return render_template('test-4.html')

@app.route("/test-4/auth-wall")

def test_4_auth_wall():
	from flask import session
	try:
		print "This is the session:", session['username']
		return "You made it past the auth wall, congrats mother fux."
	except:
		return "You are not authorized to be here dude."

@app.route("/logout")
def logout():
	from flask import session, redirect, url_for
	session.pop('username', None)
	return redirect(url_for('hello'))
