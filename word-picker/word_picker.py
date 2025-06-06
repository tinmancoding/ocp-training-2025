from flask import Flask

app = Flask(__name__)

choices = ["first", "second", "third"]

@app.route('/')
def pick_word():
    return choices[0]