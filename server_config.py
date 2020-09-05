import os

TESTING = True
DEBUG = True
FLASK_ENV = 'development'

UPLOAD_FOLDER = os.path.dirname(os.getcwd() + "/image_uploads/")
DOWNLOAD_FOLDER = os.path.dirname(os.getcwd() + "/image_downloads/")