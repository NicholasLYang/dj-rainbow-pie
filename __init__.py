import os
import utils
from flask import (Flask,
                   render_template,
                   session,
                   request,
                   redirect,
                   url_for,
                   send_from_directory)
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

flask_path = os.path.dirname(__file__)

@app.route('/')
@app.route('/home')
def home():
    return send_from_directory('templates', 'ringtone.mp3')

@app.route('/get_mp3/<file_name>')
def get_mp3(file_name):
    return send_from_directory('mp3s', file_name)


if __name__ == '__main__':
    app.run()
