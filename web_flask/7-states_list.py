#!/usr/bin/python3
""" Script that starts a Flask web application. """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontex
def close_session(exception):
    """ Remove the current SQLAlchemy Session. """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all State objects."""
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
