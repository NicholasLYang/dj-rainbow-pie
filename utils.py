

def file_name_to_name(file_name):
    dot_index = file_name.find('.')
    name = file_name[:dot_index]
    words = name.split('_')
    return ' '.join(words).title()

def name_to_file_name(name):
    file_name = ''
    words = name.split(' ')
    return '_'.join(words).lower() + '.mp3'


