#!/usr/bin/python3
"""Module task_04_flask: Define Develop a simple API using Python with Flask"""


from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "jane",
             "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John",
             "age": 30, "city": "New York"}
}


@app.route('/', methods=['GET'])
def home():
    """This route responds with a welcome message
    when the root URL is accessed."""
    return jsonify("Welcome to the Flask API!")


@app.route('/data', methods=['GET'])
def get_users():
    """Route to get a list of all usernames"""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status', methods=['GET'])
def status():
    """This route is used to check the status of the API.
    It responds with "OK"."""
    return jsonify("OK")


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """Route to get details of a specific user by username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Route to add a new user."""
    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == '__main__':
    """Main entry point of the application."""
    app.run(debug=True)
