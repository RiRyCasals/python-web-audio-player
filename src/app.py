import os
from flask import Flask, render_template, redirect, send_from_directory

dir_name = os.path.dirname(__file__)
music_path = dir_name + '/music/sample.wav'

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
    return render_template('home.html', music_path=music_path)

@app.route(dir_name + '/music/<path>')
def send_audio_data(path):
    return send_from_directory('music', path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
