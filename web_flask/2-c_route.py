#!/usr/bin/python3
""" Script to launch a Flask app with three routes """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def welcome():
    """ Returns a welcome message. """
    return 'Hello HBNB!'

@app.route('/hbnb')
def show_hbnb():
    """ Returns HBNB text. """
    return 'HBNB'

@app.route('/c/<text>')
def show_c(text):
    """ Display C followed by the value of the text variable. """
    return 'C {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
