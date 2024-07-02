#!/usr/bin/env python3
"""
This module provides a basic Flask application.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the index page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
