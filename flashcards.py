from flask import Flask, render_template
from model import db

# Flask constructor
# Creates a global Flask application object
# The name of the application, this '__name__' variable contains the name of the current module which
# in our case is the name of the current python file, which is 'flashcards'.
app = Flask(__name__) 

# A view function. '@' we use to decorate our welcome function, by assigning a URL to our function
@app.route("/")
def welcome():
    return render_template(
        "welcome.html", 
        message = 'Here is a meesage from the view.')

@app.route("/card")
def card_view():
    card = db[0]
    return render_template("card.html", card=card)

counter = 0
@app.route("/count_views")
def count_views():
    global counter #We use global, because the variable is declared outside the local scope 
    counter += 1
    return "This page was servers " + str(counter) + " times." 