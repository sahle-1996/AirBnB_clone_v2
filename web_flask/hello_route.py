#!/usr/bin/python3
""" Script to initialize a Flask web application """

from flask import Flask

app = Flask(__name__)

#Define the route for the root URL '/'
@app.route('/airbnb-onepage/', strict_slashes=False)
def greet():
    """ Returns a greeting message. """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
