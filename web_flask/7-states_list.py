#!/usr/bin/python3
""" 7. Start a Flask web application with a specific route. """

from flask import Flask
from flask import render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """Renders a simple template."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
