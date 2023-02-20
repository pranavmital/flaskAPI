from flask import Flask
import random

app_variable = Flask(__name__)

@app_variable.route("/")
def hello_world():
    print("Home path reached!")
    return "<p>Hello, World!</p>"

@app_variable.route("/a") #custom path
def path_a():
    print("Random number path reached!")
    custom_string = str(random.randint(10,1000))
    return "<p>Hello, {}</p>".format(custom_string)

# learning: it takes very little code to build this using flask/python!