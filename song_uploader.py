import utils, os
from werkzeug.utils import secure_filename

def upload_song(mp3, album, file_name, mp3_path, album_path):
    if not utils.verify_extension(mp3.filename, ".mp3"):
        raise NameError(mp3.filename)
    if not utils.verify_extension(album.filename, ".png"):
        raise NameError(album.filename)

    secured_name = secure_filename(file_name)
    secured_file_name = secured_name.lower()
    secured_mp3_name = secured_file_name + '.mp3'
    secured_album_name = secured_file_name + '.png'

    secured_mp3_path = os.path.join(mp3_path, secured_mp3_name)
    secured_album_path = os.path.join(album_path, secured_album_name)
    mp3.save(secured_mp3_path)
    album.save(secured_album_path)


