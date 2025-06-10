from flask import Flask
from random import choice

app = Flask(__name__)

choices = ["first", "second", "third"]

@app.route('/')
def pick_word():
    return choice(choices)