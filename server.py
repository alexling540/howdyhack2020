from flask import Flask, render_template, send_from_directory

app = Flask(__name__,
    template_folder='build',
    static_folder='build/static',
    static_url_path='/build/static'
)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/static/js/<path:path>")
def send_static_js(path):
    return send_from_directory('build/static/js', path)

@app.route("/static/css/<path:path>")
def send_static_css(path):
    return send_from_directory('build/static/css', path)

@app.route("/<path:path>")
def send_static(path):
    return send_from_directory('build', path)

if __name__ == "__main__":
    app.run(debug=True)