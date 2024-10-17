#!/usr/bin/python3
"""Module task_05_basic_security: Define API security and
Authentification techniques"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password123"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("adminpassword"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify user credentials for basic authentication.

    Args:
        username (str): Username provided by the client.
        password (str): Password provided by the client.

    Returns:
        str: Username if authentication is successful, otherwise None.
    """
    if username in users and check_password_hash(users[username]
                                                 ['password'], password):
        return username


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    Route protected by basic authentication.
    Accessible only if valid username and password are provided.
    
    Returns:
        Response: JSON response with an access granted message
    """
    return jsonify({"message": "Basic Auth: Access Granted"})


@app.route('/login', methods=['POST'])
def login():
    """
    Login route to authenticate users and generate a JWT access token.

    Request Body:
        - username (str): Username of the user.
        - password (str): Password of the user.

    Returns:
        Response: A JSON response containing the JWT access token if 
        credentials are valid.
                 Returns an error message if credentials are invalid.
    """
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users and check_password_hash(users[username]
                                                 ['password'], password):
        access_token = create_access_token(identity={"username": username,
                                                     "role": users[username]
                                                     ['role']})
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    Route protected by JWT authentication.
    Accessible only if a valid JWT token is provided.

    Returns:
        Response: A JSON response with an access granted message and the
        identity of the current user.
    """
    current_user = get_jwt_identity()
    return jsonify({"message": "JWT Auth: Access Granted",
                    "user": current_user})


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    Admin-only route protected by JWT authentication.
    Accessible only by users with the 'admin' role.

    Returns:
        Response: A JSON response with an access granted message for admins.
                 Returns an error message if the user is not an admin.
    """
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle missing or invalid JWT token errors.

    Args:
        err (str): The error message describing the issue.

    Returns:
        Response: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid JWT token errors.

    Args:
        err (str): The error message describing the issue.

    Returns:
        Response: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle expired JWT token errors.

    Args:
        err (str): The error message describing the issue.

    Returns:
        Response: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handle revoked JWT token errors.

    Args:
        err (str): The error message describing the issue.

    Returns:
        Response: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle errors where a fresh JWT token is required.

    Args:
        err (str): The error message describing the issue.

    Returns:
        Response: A JSON response with an error message and a 401 status code.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run(debug=True)
