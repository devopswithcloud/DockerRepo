import os
from flask import Flask, render_template
server = Flask(__name__)

@server.route("/")
def welcome():
    return render_template("webpage.html")

@server.route('/openshift')
def hello():
    return 'Openshift is easy to learn'

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8080)
