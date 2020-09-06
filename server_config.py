import os

TESTING = True
DEBUG = True
FLASK_ENV = 'development'

UPLOAD_FOLDER = os.path.join(os.getcwd(), "image_uploads")
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "image_downloads")