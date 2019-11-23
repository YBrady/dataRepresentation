#!flask/bin/python
from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='', static_folder='.')
#app = Flask(__name__)

acts = [
    {"id": 1, "name":"Joe", "totalVotes": 3},
    {"id": 2, "name": "John", "totalVotes": 4},
]

nextID = 4

#@app.route('/')
#def index():
#    return "Hello, World"


@app.route('/acts')
def getAll():
    return jsonify(acts)
    # Test in CURL
    # curl http: // 127.0.0.1: 5000/acts


@app.route('/acts/<int:id>')
def findByID(id):
    foundActs = list(filter(lambda a: a['id'] == id, acts))
    if len(foundActs) == 0:
        return jsonify({}), 204
    else:
        return jsonify(foundActs[0])
    # Test in CURL
    # curl "http://127.0.0.1:5000/acts/1"


@app.route('/acts', methods=['POST'])
def create():
    global nextID
    if not request.json:
        abort(400)
        # Other checking - that it is properly formatted etc
    act = {
        "id": nextID,
        "name": request.json['Name'],
        "totalVotes":0
    }
    nextID += 1
    acts.append(act)
    return jsonify(act)
    # return "in create"
    # Test in CURL
    # curl -X POST "http://127.0.0.1:5000/books"
    # curl -H "Content-Type:application/json" -X POST -d "{\Name\":\"Mary\"}" http://127.0.0.1:5000/acts

@app.route('/acts/<int:id>', methods=['DELETE'])
def delete(id):
    foundActs = list(filter(lambda b: b['id'] == id, acts))
    if len(foundActs) == 0:
        abort(404)
    acts.remove(foundActs[0])
    return jsonify({"done": True})
    # Test in CURL
    # curl -X DELETE "http://127.0.0.1:5000/acts/1"

@app.route('/votes/<int:actId>', methods = ['POST'])
def addVote(actId):
    foundActs = list(filter(lambda t: t['id'] == actId, acts))
    if len(foundActs) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if not 'votes' in request.json or type(request.json['votes']) is not int:
        abort(401)
    newVotes = request.json['votes']
    foundActs[0]['totalVotes']+= newVotes
    return  jsonify(foundActs[0])
    # Test in curl
    # curl -X POST http://127.0.0.1:5000/votes/123


@app.route('/votes/leaderboard')
def getLeaderBoard():
    acts.sort(key=lambda x: x['totalVotes'], reverse=True)
    #return "in get leaderboard"
    return jsonify(acts)
    # Test in curl
    # curl http://127.0.0.1:5000/votes/leaderboard

if __name__ == '__main__':
    app.run(debug=True)
