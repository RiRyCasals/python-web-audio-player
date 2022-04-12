import os
from flask import Flask, render_template, redirect

dir_name = os.path.dirname(__file__)

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

#login require
@app.route('/')
def index():
    return redirect('/home')

#login require
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
