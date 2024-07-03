#!/usr/bin/env python3
"""
5-app.py


Requirements:
- Ubuntu 18.04 LTS
- Python 3.7
- pycodestyle (version 2.5)
- README.md file present
- Python file ends with a new line
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz

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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Function to get a user dictionary by ID.

    Returns:
    - User dictionary or None if the user ID is not found.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
    Function to be executed before each request.
    Sets g.user to the user dictionary if a valid user is found.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Function to determine the best-matching language for the user based on

    Returns:
    - Best-matching language code ('en' or 'fr').
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Route for the index page.

    Returns:
    - Rendered template '5-index.html' with translated messages.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
