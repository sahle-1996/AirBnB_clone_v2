#!/usr/bin/python3
""" Script to launch a Flask web application with two routes """

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """ Returns a welcome message. """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns an HBNB message. """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
