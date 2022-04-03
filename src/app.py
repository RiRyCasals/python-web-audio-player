import os
from flask import Flask, render_template, Response

dir_name = os.path.dirname(__file__)
file_path = '/music/example.mp3'
buffer_size = 1024

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           file_path=file_path)

@app.route('/music/<path:file_name>')
def stream_audio(file_name):
    print(dir_name + file_name)
    def generate():
        with open(dir_name + '/music/' + file_name, 'rb') as f:
            data = f.read(buffer_size)
            while data:
                yield data
                data = f.read(buffer_size)
    return Response(generate(), mimetype='audio/x-wav')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
