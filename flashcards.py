from flask import Flask
from datetime import datetime

# Flask constructor
# Creates a global Flask application object
# The name of the application, this '__name__' variable contains the name of the current module which
# in our case is the name of the current python file, which is 'flashcards'.
app = Flask(__name__) 

# A view function. '@' we use to decorate our welcome function, by assigning a URL to our function
@app.route("/")
def welcome():
    return "Welcome to my Flash cards application!"

@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())

counter = 0
@app.route("/count_views")
def count_views():
    global counter #We use global, because the variable is declared outside the local scope 
    counter += 1
    return "This page was servers " + str(counter) + " times." 
