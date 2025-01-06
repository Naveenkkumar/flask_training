from flask import Flask
import pickle

app = Flask(__name__) # create an app instance



@app.route("/ping", methods=["GET"])
def ping():
    return "pong"

