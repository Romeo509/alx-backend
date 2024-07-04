#!/usr/bin/env python3
"""
4-app.py

Flask app demonstrating internationalization (i18n) using Flask-Babel.

Requirements:
- Ubuntu 18.04 LTS
- Python 3.7
- pycodestyle (version 2.5)
- README.md file present
- Python file ends with a new line
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

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
"""Testing documentation at this side"""


@babel.localeselector
def get_locale():
    """
    Function to determine the best-matching language for the user based on
    the 'locale' query parameter or the Accept-Language header in the request.

    Returns:
    - Best-matching language code ('en' or 'fr').
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Route for the index page.

    Returns:
    - Rendered template '4-index.html' with translated messages.
    """
    return render_template(
        '4-index.html', title=_('home_title'), header=_('home_header')
    )


if __name__ == '__main__':
    app.run(debug=True)
