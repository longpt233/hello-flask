from flask import Flask
from flask import render_template
from flask import json
from flask import request
app = Flask(__name__)

@app.route("/")
def main():
  return "Welcome"

@app.route("/home")
def home():
  return render_template('index.html')

@app.route('/sign-up')
def showsignup():
  return render_template('signup.html')

@app.route('/sign-up',methods=['POST'])
def signup():
 
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    print("[INFO] signup receive ",_name," ",_email," ",_password)
 
    # validate the received values
    if _name and _email and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


if __name__ == "__main__":
  app.run()