#!/usr/bin/env python3
"""
Basic Babel setup
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Instantiate Babel object
babel = Babel(app)


# Config class
class Config:
    """
    configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Use Config to set Babel's default locale and timezone
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    determine the best match with our supported languages
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def index():
    """
    Renders index.html template
    """
    return render_template("3-index.html")


if __name__ == '__main__':
    app.run(debug=True)
