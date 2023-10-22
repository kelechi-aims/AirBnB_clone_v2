#!/usr/bin/python3
""" Script that starts a Flask web application. """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_state(id=None):
    """lists states from storage engine"""
    if id:
        states = storage.all(State)
        key = 'State.' + id
        if key in states:
            state = states[key]
        else:
            state = None
        states = []
    else:
        states = list(storage.all(State).values())
    return render_template('9-states.html', **locals())



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

