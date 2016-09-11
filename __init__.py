import os
import utils, song_uploader
from flask import (Flask,
                   render_template,
                   session,
                   request,
                   redirect,
                   url_for,
                   send_from_directory)
import audio_analyzer

app = Flask(__name__)


FLASK_PATH = os.path.dirname(__file__)
STATIC_PATH = os.path.join(FLASK_PATH, 'static')
MP3_PATH = os.path.join(FLASK_PATH, 'mp3s')
ALBUM_PATH = os.path.join(STATIC_PATH, 'albums')
TEMPLATES_PATH = os.path.join(FLASK_PATH, 'templates')



@app.route('/')
@app.route('/index')
def index():
    albums = os.listdir(ALBUM_PATH)
    mp3_file_names = os.listdir(MP3_PATH)
    mp3_names = map(utils.file_name_to_name, mp3_file_names)
    songs = zip(mp3_file_names, mp3_names, albums)
    return render_template('index.html',
                           songs=songs)

@app.route('/read_mp3/<file_name>')
def read_mp3(file_name):
    file_path = os.path.join(MP3_PATH, file_name)
    audio_analyzer.read_mp3(file_path)
    return redirect(url_for('index'))

@app.route('/delete_song/<mp3_name>')
def delete_song(mp3_name):
    mp3_path = os.path.join(MP3_PATH, mp3_name)
    dot_index = mp3_name.find('.')
    album_name = mp3_path[0:dot_index] + ".png"
    print album_name
    album_path = os.path.join(ALBUM_PATH, album_name)
    os.remove(mp3_path)
    os.remove(album_path)
    return redirect(url_for('index'))

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        mp3 = request.files['mp3']
        album = request.files['album-cover']
        file_name = request.form['name']
        song_uploader.upload_song(mp3, album, file_name, MP3_PATH, ALBUM_PATH)
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()
