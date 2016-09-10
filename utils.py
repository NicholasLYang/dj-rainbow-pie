

def file_name_to_name(file_name):
    dot_index = file_name.find('.')
    name = file_name[:dot_index]
    words = name.split('_')
    return ' '.join(words).title()

def name_to_file_name(name):
    file_name = ''
    words = name.split(' ')
    return '_'.join(words).lower() + '.mp3'


def color_wheel(wheel_pos):
  if wheel_pos < 85:
    return [wheel_pos * 3, 255 - wheel_pos * 3, 0]
  elif wheel_pos < 170:
    wheel_pos = wheel_pos - 85
    return [255 - wheel_pos * 3, 0, wheel_pos * 3]
  else:
    wheel_pos = wheel_pos - 170;
    return [0, wheel_pos * 3, 255 - wheel_pos * 3]


def verify_file_name(file_name):
    dot_index =file_name.find('.')
    extension = file_name[dot_index:]
    return extension == '.mp3'
