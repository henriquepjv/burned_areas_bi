import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)


login_manager = LoginManager(app)
login_manager.init_app(app)

@app.route('/')
def index():
    '''Returns a static HTML page'''

    return render_template('index.html')
