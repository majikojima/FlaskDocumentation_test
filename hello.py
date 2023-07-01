from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Index Page</p>"

@app.route("/hello")
def hello():
    a = 1 + 1
    return f"<p>Hello World!</p>a={a}"

@app.route("/zarigani")
def zarigani():
    name = "ザリガニ"
    return f"<p>Hello {name}!</p>"