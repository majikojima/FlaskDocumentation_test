from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    a = 1 + 1
    return "<p>Hello World!</p>a"