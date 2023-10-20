#!/usr/bin/python3
'''Script that starts a Flask web application'''
from flask import Flask


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
