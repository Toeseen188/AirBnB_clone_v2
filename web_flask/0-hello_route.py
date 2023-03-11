#!/usr/bin/python3
" Start a server in flask "

from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    " index page "
    return 'Hello HBNB!'
