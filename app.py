from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

from database import *	

@app.route('/')
def homepage():
	return render_template("homepage.html")

@app.route('/about')
def aboutpage():
	return render_template("about.html")

@app.route('/login')
def loginpage():
	return render_template("login.html")

@app.route('/signin')
def signinpage():
	return render_template("signin.html")

@app.route('/login', methods=['POST'])
def login():
    user = get_user(request.form['username'])
    if user != None and user.verify_password(request.form["password_hash"]):
        login_session['name'] = user.username
        return home()


@app.route('/signup', methods=['POST'])
def signup():
    #check that username isn't already taken
    user = get_user(request.form['username'])
    if user == None:
        add_user(request.form['username'],request.form['password'], request.form['gender'])
    return home()




if __name__ == '__main__':
    app.run(debug=True)