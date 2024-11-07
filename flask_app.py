
# A very simple Flask Hello World app for you to get started with...

from datetime import datetime

from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():

    DAYNAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    dayname = DAYNAMES[datetime.now().weekday()]
    return f"<p>foobar, world! Happy {dayname}.</p>"

