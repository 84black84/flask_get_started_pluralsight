from flask import Flask
# from flask_debugtoolbar import DebugToolbarExtension

# Flask constructor
# Creates a global Flask application object
# The name of the application, this '__name__' variable contains the name of the current module which
# in our case is the name of the current python file, which is 'flashcards'.
app = Flask(__name__)
# app.debug = True
# app.config['SECRET_KEY'] = '3945ec69-1750-4912-94da-378366941c50'
# toolbar = DebugToolbarExtension(app)

import FlashCardsWebProject.views
import FlashCardsWebProject.cardApi