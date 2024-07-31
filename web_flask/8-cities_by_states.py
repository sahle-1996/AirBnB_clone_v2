#!/usr/bin/python3
"""
Initialize a Flask web application
"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def show_cities():
    """Displays states and their cities in alphabetical order"""
    all_states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=all_states)


@app.teardown_appcontext
def close_storage(exception):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
