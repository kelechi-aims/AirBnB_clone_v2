#!/usr/bin/python3
""" Script that starts a Flask web application. """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states', strict_slashes=False)
def states_items():
    """ Render a template with the list of states """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_state(id):
    """ Render a template with the list of cities of a state """
    state = storage.get(State, id)
    if state is None:
        return render_template('9-states.html', state=None, cities=None)
    cities = storage.all(City).values()
    cities = [city for city in cities if city.state_id == id]
    return render_template('9-states.html', state=state, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
