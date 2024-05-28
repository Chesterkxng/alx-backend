#!/usr/bin/env python3
"""
First you will setup a basic Flask app in 0-app.py. Create a single
route and an index.html template that simply outputs “Welcome to Holberton”
as page title (<title>) and “Hello world” as header (<h1>).
"""
from flask import (
    Flask,
    render_template,
)
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

# Class configuration
class Config:
    """
    configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# use defined configuration
app.config.from_object(Config)

@app.route("/", strict_slashes=False)
def hello():
    """ function that return the hello world page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
