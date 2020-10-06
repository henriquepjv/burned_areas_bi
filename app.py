from flask import Flask, render_template, request, send_from_directory
import json
import os

# Initialize the Flask app
app = Flask(__name__)

# Used to toggle debug statements
app.debug = False

# Load configuration
app.config.from_object('config.BaseConfig')

@app.route('/')
def index():
    '''Returns a static HTML page'''

    return render_template('index.html')


@app.route('/favicon.ico', methods=['GET'])
def getfavicon():
    '''Returns path of the favicon to be rendered'''

    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run()
