import os
from flask import Flask, render_template, send_from_directory

file_path = '/music/example.mp3'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           file_path=file_path)

@app.route('/music/<path:file_name>')
def send_audio_src(file_name):
    return send_from_directory('music', file_name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
