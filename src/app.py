from flask import Flask, jsonify, request
from flask_cors import CORS


# Instantiation
app = Flask(__name__)


# Settings
CORS(app)

# Database


# Routes
@app.route('/users', methods=['POST'])
def createUser():
  return "jsonify(str(ObjectId(id)))"


@app.route('/users', methods=['GET'])
def getUsers():
    return "jsonify(users)"

@app.route('/users/<id>', methods=['GET'])
def getUser(id):
  return "jsonify({'_id': str(ObjectId(user['_id'])),'name': user['name'],'email': user['email'], 'password': user['password']"


@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
  return "jsonify({'message': 'User Deleted'})"

@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
  return "jsonify({'message': 'User Updated'})"

if __name__ == "__main__":
    app.run(debug=True)