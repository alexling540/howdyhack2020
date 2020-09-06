import os
import re
import time
from shutil import copyfile
from flask import send_from_directory
from server_config import UPLOAD_FOLDER, DOWNLOAD_FOLDER
from faceRecognition import glasses_stache

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


def proccess_file(filename):
    copyfile(get_path(filename), get_path(filename, False))
    glasses_stache(get_path(filename, False))
    os.remove(get_path(filename))


def download_file(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)


def init_folders():
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)


def delete_old_files(threshold):
    now = time.time()
    for file in os.listdir(DOWNLOAD_FOLDER):
        full_path = get_path(file, False)
        if now - os.path.getmtime(full_path) >= 300:
            os.remove(full_path)
