from PIL import Image
import sys
import os


def get_dest_file_name(dest, file):
    dest_file = dest + os.path.splitext(file)[0] + '.png'

    seq = 0
    while os.path.exists(dest_file):
        dest_file = dest + os.path.splitext(file)[0] + str(seq) + '.png'
        seq += 1
    return dest_file


try:
    source = sys.argv[1]
    dest = sys.argv[2]
except IndexError as e:
    print(str(e) + '\nPlease provide source and destination file')
    exit(-1)

if not os.path.exists(source):
    print(source + 'doesn\'t exist')

if not os.path.exists(dest):
    os.mkdir(dest)

for file in os.listdir(source):
    file_abs = os.path.abspath(source + file)
    if os.path.splitext(file_abs)[1] == '.jpg':
        img = Image.open(file_abs)
        dest_file = get_dest_file_name(dest, file)
        img.save(dest_file, format='png')
