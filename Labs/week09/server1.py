#!flask/bin/python
from flask import Flask, jsonify, request, abort
# This is the mySQL connector
from bookDAO import bookDAO

app = Flask(__name__, static_url_path='', static_folder='.')
#app = Flask(__name__)

#books=[
#    {"id" :1,
#    "Title": "Harry Potter and The Philosophers Stone",
#    "Author": "JK Rowling",
#    "Price": 1000},
#    {"id" : 2,
#    "Title": "Harry Potter and The Chamber of Secrets",
#    "Author": "JK Rowling",
#    "Price": 1100},
#    {"id" : 3,
#    "Title": "Harry Potter and The Prison of Azkaban",
#    "Author": "JK Rowling",
#    "Price": 950}
#]

#nextID = 4

#@app.route('/')
#def index():
#    return "Hello, World"

@app.route('/books')
def getAll():
    results = bookDAO.getAll()
    return jsonify(results)
    # Test in CURL
    # curl http: // 127.0.0.1: 5000/books


@app.route('/books/<int:id>')
def findByID(id):
    foundBook = bookDAO.findByID(id)
    return jsonify(foundBook)
    # Test in CURL
    # curl "http://127.0.0.1:5000/books/1"


@app.route('/books', methods=['POST'])
def create():

    if not request.json:
        abort(400)
    # Other checking - that it is properly formatted etc
    book = {
        "Title": request.json['Title'],
        "Author": request.json['Author'],
        "Price": request.json['Price']
    }
    values = (book['Title'], book['Author'],book['Price'])
    newId =  bookDAO.create(values)
    book['id']= newId
    return jsonify(book)
    # Test in CURL
    # curl -X POST "http://127.0.0.1:5000/books"
   #  curl -H "Content-Type:application/json" -X POST -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":2000}" http://127.0.0.1:5000/books


@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBook = bookDAO.findByID(id)
    # Pre-DAO code commented out here
    #foundBooks = list(filter(lambda b: b['id']== id, books))
    #if len(foundBooks)==0:
    if not foundBook:
        abort(404)
    #foundBook = foundBooks[0]
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)

    if 'Title' in reqJson:
        foundBook['Title'] = reqJson['Title']
    if 'Author' in reqJson:
        foundBook['Author'] = reqJson['Author']
    if 'Price' in reqJson:
        foundBook['Price'] = reqJson['Price']
    values = (foundBook['Title'], foundBook['Author'],
              foundBook['Price'], foundBook['id'])
    # write to data
    bookDAO.update(values)
    return jsonify(foundBook)
    # Test in CURL
    # curl -X PUT "http://127.0.0.1:5000/books/123"
    # curl -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":2000}" http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    # Commented out the code needed before DAO 
    #foundBooks = list(filter(lambda b: b['id'] == id, books))
    #if len(foundBooks) == 0:
    #    abort(404)
    #books.remove(foundBooks[0])
    bookDAO.delete(id)
    return jsonify({"done":True})
    # Test in CURL
    # curl -X DELETE "http://127.0.0.1:5000/books/1"

if __name__ == '__main__':
    app.run(debug=True)
