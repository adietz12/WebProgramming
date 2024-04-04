from flask import Flask, jsonify, send_from_directory, render_template, request, redirect
from mongita import MongitaClientDisk


app = Flask(__name__)

client = MongitaClientDisk()
db = client.quotes_db
collection = db.quotes

@app.route('/', methods=["GET"])
@app.route('/quotes', methods=["GET"])
def get_quotes():
    
    data = list(collection.find({}))

    return render_template('quotes.html', quotes=data)

@app.route('/delete/<id>', methods=["GET"])
def delete_quote(id=None):

    collection.delete_one({"_id": id})

    return redirect('/')

# TODO
@app.route('/create', methods=["GET"])
def create_quote():
    return render_template('newQuote.html')

@app.route('/create', methods=["POST"])
def add_quote():
    quote = request.form.get('quote', None)
    author = request.form.get('author', None)
    collection.insert_one({"text": quote, "author": author})
    return redirect('/')

@app.route('/edit/<id>', methods=["GET"])
def edit_quote(id=None):
    item = collection.find_one({"_id": id})
    return render_template('editQuote.html', quote=item)


@app.route('/edit/<id>', methods=["POST"])
def post_edit_quote(id=None):
    quote = request.form.get('quote', None)
    author = request.form.get('author', None)
    # collection.update_one({"_id": id}, { "$set": {'text': quote } })
    # collection.delete_one({"_id": id})
    # collection.insert_one({"text": quote, "author": author})
    collection.update_one({"_id": id}, { "$set": {'text': quote, 'author': author } })
    return redirect('/')