#!/usr/bin/python3
"""
Start a server in flask and route to ('/hbnb')
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    " index page "
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ route /hbnb """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
