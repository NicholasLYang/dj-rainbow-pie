import os
from flask import (Flask,
                   render_template,
                   session,
                   request,
                   redirect,
                   url_for,
                   send_from_directory)


app = Flask(__name__)

flask_path = os.path.dirname(__file__)

@app.route("/")
@app.route("/home")
def home():
    return send_from_directory('templates', 'ringtone.mp3')



if __name__ == "__main__":
    app.run()
