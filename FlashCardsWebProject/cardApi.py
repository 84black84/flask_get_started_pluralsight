from FlashCardsWebProject import app
from FlashCardsWebProject.model import db
from flask import jsonify, abort

## ----- API Methods -----
@app.route("/api/card/")
def api_card_list():
    return jsonify(db)
3
@app.route('/api/card/<int:index>')
def api_card_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)