#!flask/bin/python
from flask import Flask , jsonify ,abort ,request
import json
from tinydb import TinyDB, Query

app = Flask(__name__)

#just wyswietl strone
@app.route('/')
def index():
    return  "<h1>!HELLO WORLD!"

#add data trouch GET and show everything
@app.route('/list', methods=['GET', 'POST'])
def parse_request():
    db = TinyDB('db.json')
    User = Query()
    x = db.search(User)
    data = request.args
    db.insert(data)
    return jsonify(x)


#przesylanie danych jako JSON with POST
@app.route('/add', methods=['POST'])
def hello():
    db = TinyDB('db.json')
    imp = request.get_json()
    db.insert(imp)
    return jsonify(request.get_json())

#wyszukiwanie w bazie danych 
@app.route('/serch', methods=['GET', 'POST'])
def parse_request():
    pass
    #do edycji 
    """
        db = TinyDB('db.json')
    User = Query()
    x = db.search(User)
    data = request.args
    db.insert(data)
    return jsonify(x)

    """

if __name__ == '__main__':
    app.run(debug=True)

