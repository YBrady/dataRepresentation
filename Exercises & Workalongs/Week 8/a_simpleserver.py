#!flask/bin/python
from flask import Flask
from flask_cors import CORS # to allow cross site scripting if there is a problem with localhost:5000

app = Flask(__name__, static_url_path= '',static_folder='.')
#app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello, World"

@app.route('/book/<int:id>')
def getBook(id):
    return "You want book with " + str(id)

if __name__ == '__main__':
    app.run(debug=True)
