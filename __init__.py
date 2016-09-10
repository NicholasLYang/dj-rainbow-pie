import os
import utils
from flask import (Flask,
                   render_template,
                   session,
                   request,
                   redirect,
                   url_for,
                   send_from_directory)



app = Flask(__name__)

FLASK_PATH = os.path.dirname(__file__)
MP3_PATH = os.path.join(FLASK_PATH, 'mp3s')
TEMPLATES_PATH = os.path.join(FLASK_PATH, 'templates')

@app.route('/')
@app.route('/home')
def home():
    return send_from_directory(TEMPLATES_PATH, 'ringtone.mp3')

@app.route('/get_mp3/<file_name>')
def get_mp3(file_name):
    return send_from_directory(MP3_PATH, file_name)

@app.route('/index')
def index():
    mp3_file_names = os.listdir(MP3_PATH)
    mp3_names = map(utils.file_name_to_name, mp3_file_names)
    mp3s = zip(mp3_file_names, mp3_names)
    return render_template('index.html',
                           mp3s=mp3s)


if __name__ == '__main__':
    app.debug = True
    app.run()
