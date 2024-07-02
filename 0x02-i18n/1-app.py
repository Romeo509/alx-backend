#!/usr/bin/env python3
"""
1-app.py

This script demonstrates the setup of a Flask app with Flask-Babel extension.

Requirements:
- Ubuntu 18.04 LTS
- Python 3.7
- pycodestyle (version 2.5)
- README.md file present
- Python file ends with a new line
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class for Flask app configuration.

    Attributes:
    - LANGUAGES: List of available languages.
    - BABEL_DEFAULT_LOCALE: Default locale for Babel.
    - BABEL_DEFAULT_TIMEZONE: Default timezone for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """
    Route for the index page.

    Returns:
    - Rendered template '1-index.html'.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
