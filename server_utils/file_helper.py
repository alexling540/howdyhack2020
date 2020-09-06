import os
import re
import time
import shutil
from flask import send_from_directory
from server_config import UPLOAD_FOLDER, DOWNLOAD_FOLDER
from server_utils.image_processing import faceRecognition

# Helper Functions
file_pattern = re.compile("^[\w\-. ]+.(png|jpe?g|tiff)$", re.IGNORECASE)


def is_valid_file(filename):
    return file_pattern.match(filename)


def get_path(filename, upload=True):
    if upload:
        return os.path.join(UPLOAD_FOLDER, filename)
    return os.path.join(DOWNLOAD_FOLDER, filename)


def upload_file(file, filename):
    file.save(get_path(filename))


def proccess_file_face(filename):
    shutil.copyfile(get_path(filename), get_path(filename, False))
    faceRecognition.rectangles(get_path(filename, False))
    os.remove(get_path(filename))

    
def proccess_file_disguise(filename, style="regular"):
    shutil.copyfile(get_path(filename), get_path(filename, False))
    faceRecognition.glasses_stache(get_path(filename, False), style)
    os.remove(get_path(filename))


def download_file(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)


def init_folders():
    if os.path.exists(UPLOAD_FOLDER):
        shutil.rmtree(UPLOAD_FOLDER)
    os.makedirs(UPLOAD_FOLDER)
    with open(os.path.join(UPLOAD_FOLDER, '.gitkeep'), 'w') as fp: 
        pass
    if os.path.exists(DOWNLOAD_FOLDER):
        shutil.rmtree(DOWNLOAD_FOLDER)
    os.makedirs(DOWNLOAD_FOLDER)
    with open(os.path.join(DOWNLOAD_FOLDER, '.gitkeep'), 'w') as fp: 
        pass


def delete_old_files():
    now = time.time()
    print(now)
    for file in os.listdir(DOWNLOAD_FOLDER):
        if file != '.gitkeep':
            full_path = get_path(file, False)
            print(full_path)
            if now - os.path.getmtime(full_path) >= 120:
                os.remove(full_path)
