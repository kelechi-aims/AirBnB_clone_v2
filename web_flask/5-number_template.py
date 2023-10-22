#!/usr/bin/python3
'''Script that starts a Flask web application'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''Route handler function for the root URL ("/")'''
    return "Hello HBNB!"


@app.route('/hnbn', strict_slashes=False)
def hbnb():
    ''' Route  handler function for the "/hbnb" URL.'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    ''' Route handler function for the "/c/<text>" URL pattern.'''
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    ''' Route handler function for the "/python/<text>" URL pattern.'''
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """ Route handler function for the '/number/<n>' URL pattern."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Route handler function for the "/number_template/<n>" URL pattern. """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
