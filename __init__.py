import os
import utils, mp3_uploader
from flask import (Flask,
                   render_template,
                   session,
                   request,
                   redirect,
                   url_for,
                   send_from_directory)
from werkzeug.utils import secure_filename


app = Flask(__name__)

FLASK_PATH = os.path.dirname(__file__)
MP3_PATH = os.path.join(FLASK_PATH, 'mp3s')
TEMPLATES_PATH = os.path.join(FLASK_PATH, 'templates')

@app.route('/')
@app.route('/index')
def index():
    mp3_file_names = os.listdir(MP3_PATH)
    mp3_names = map(utils.file_name_to_name, mp3_file_names)
    mp3s = zip(mp3_file_names, mp3_names)
    return render_template('index.html',
                           mp3s=mp3s)

@app.route('/get_mp3/<file_name>')
def get_mp3(file_name):
    return send_from_directory(MP3_PATH, file_name)

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        file = request.files['file']
        file_name = request.form['name']
        mp3_uploader.upload_mp3(file, file_name, MP3_PATH)
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()
