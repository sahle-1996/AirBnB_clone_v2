#!/usr/bin/python3
""" Script to start a Flask app with various routes """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def index():
    """ Returns a welcome message. """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """ Returns HBNB text. """
    return 'HBNB'

@app.route('/c/<text>')
def c_display(text):
    """ Display C followed by the value of the text variable. """
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/')
@app.route('/python/<text>')
def python_display(text='is cool'):
    """ Display Python followed by the value of the text variable. """
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>')
def number_display(n):
    """ Display number if the variable is an integer. """
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
