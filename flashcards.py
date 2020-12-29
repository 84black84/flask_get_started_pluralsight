from flask import Flask, render_template, abort, jsonify, request, redirect, url_for
from model import db, save_db

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
        cards = db
    )

counter = 0
@app.route("/count_views")
def count_views():
    global counter #We use global, because the variable is declared outside the local scope 
    counter += 1
    return "This page was servers " + str(counter) + " times." 

@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template("card.html",
                                card=card, 
                                index=index,
                                max_index=len(db) - 1
        )
    except IndexError:
        abort(404)

@app.route('/add_card', methods=["GET", "POST"])
def add_card():
    if request.method == "POST":
        # form has been submitted, process data
        card = {
            "question": request.form['question'],
            "answer": request.form['answer']
        }

        db.append(card)
        save_db()
        return redirect(url_for('card_view', index=len(db)-1))
    else:
        return render_template("add_card.html")


@app.route('/remove_card/<int:index>', methods=["GET", "POST"])
def remove_card(index):
    try:
        if request.method == "POST":
            del db[index]
            save_db()
            return redirect(url_for('welcome'))
        else:
            return render_template("remove_card.html", card=db[index])
    except IndexError:
        abort(404)

## ----- API Methods -----

@app.route("/api/card/")
def api_card_list():
    return jsonify(db)


@app.route('/api/card/<int:index>')
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)