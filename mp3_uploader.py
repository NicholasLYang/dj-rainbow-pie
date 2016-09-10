import utils, os
from werkzeug.utils import secure_filename

def upload_mp3(file, file_name, mp3_path):
    if not utils.verify_file_name(file.filename):
        raise NameError(file.filename)

    secured_name = secure_filename(file_name)
    secured_file_name = secured_name.lower() + '.mp3'

    secured_file_path = os.path.join(mp3_path, secured_file_name)
    file.save(secured_file_path)


