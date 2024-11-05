form flask import Flask

app = Flask(__name __)

@app.route("/")
def hello_world():
        return "<p>hello, world!</p>"
