#!/usr/bin/python3
""" Script to start a Flask app with redirect and default variable """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def greet():
    """ Returns a greeting message. """
    return 'Hello HBNB!'

@app.route('/hbnb')
def show_hbnb():
    """ Returns HBNB text. """
    return 'HBNB'

@app.route('/c/<text>')
def show_c(text):
    """ Display C followed by the value of the text variable. """
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/')
@app.route('/python/<text>')
def show_python(text='is cool'):
    """ Display Python followed by the value of the text variable. """
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
