from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config={"apiKey": "AIzaSyC-X4AH2AgXtdSJpT4MFkUz5sAMcdoGcso",
  "authDomain": "csisthebest-ca801.firebaseapp.com",
  "projectId": "csisthebest-ca801",
  "storageBucket": "csisthebest-ca801.appspot.com",
  "messagingSenderId": "294356865102",
  "appId": "1:294356865102:web:c8fddcc6f1b2c6f709b31f"
,"databaseURL":""}


firebase=pyrebase.initialize_app(config)
auth=firebase.auth()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
     error = ""
     if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except Exception as e:
            error = "Authentication failed"
            print(f"ERROR LOGGING IN: {e}")

     return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
   error = ""
   if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    try:
        login_session['user'] = auth.create_user_with_email_and_password(email, password)
        return redirect(url_for('signin'))
    except Exception as e:
        error = "Authentication failed"
        print(f"ERROR SIGNING UP: {e}")
   return render_template("signup.html")
    


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)