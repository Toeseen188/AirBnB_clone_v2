#!/usr/bin/python3
"""
Start a server in flask and route to ('/hbnb')
@app.route('/python/)
@app.route('/python/<text>')
@app.route('/number/int:n')
conditional statement
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    " index page "
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ route /hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """ use var in route """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ route '/python/text' where default
    text= is cool
    """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ run only if the route is converted to int"""
    return '%s is a number' % ni


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """render template """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
