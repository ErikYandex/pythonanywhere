
# A very simple Flask Hello World app for you to get started with...
import calendar

from datetime import datetime

from flask import Flask


DAYNAMES = list(calendar.day_name)


app = Flask(__name__)

@app.route("/")
def hello_world():
    dayname = DAYNAMES[datetime.now().weekday()]
    return f"<p>foobar, world! Happy {dayname}.</p>"

