# Explore the flask module and create a web server using flask and Python.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>this is the heading of my web page</h1>"

app.run()