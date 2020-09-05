import os
import re
from shutil import copyfile
from flask import Flask, request, redirect, render_template, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__,
    template_folder='build',
    static_folder='build/static',
    static_url_path='/build/static'
)

app.config["UPLOAD_FOLDER"] = os.path.dirname(os.getcwd()+ "/image_uploads/")
app.config["DOWNLOAD_FOLDER"] = os.path.dirname(os.getcwd() + "/image_downloads/")

def get_path(filename, upload=True):
    if upload:
        return os.path.join(app.config["UPLOAD_FOLDER"], filename)
    return os.path.join(app.config["DOWNLOAD_FOLDER"], filename)

# Helper Functions
file_pattern = re.compile("^[\w\-. ]+.(png|jpe?g|tiff)$", re.IGNORECASE)
def is_valid_file(filename):
    return file_pattern.match(filename)

def upload_file(file, filename):
    file.save(get_path(filename))

def proccess_file(filename):
    copyfile(get_path(filename), get_path(filename, False))
    # TODO: IMPLEMENT OPENCV
    os.remove(get_path(filename))

def download_file(filename):
    return send_from_directory(app.config["DOWNLOAD_FOLDER"], filename, as_attachment=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        
        file = request.files["file"]
        filename = file.filename

        if filename == "":
            return redirect(request.url)
        
        if file and is_valid_file(filename):
            filename = secure_filename(filename)
            upload_file(file, filename)
            proccess_file(filename)
            return download_file(filename)

    return render_template('index.html')

# Build files from React
@app.route("/static/js/<path:path>")
def send_static_js(path):
    return send_from_directory('build/static/js', path)

@app.route("/static/css/<path:path>")
def send_static_css(path):
    return send_from_directory('build/static/css', path)

@app.route("/<path:path>")
def send_static(path):
    return send_from_directory('build', path)

# Main
if __name__ == "__main__":
    app.run(debug=True)