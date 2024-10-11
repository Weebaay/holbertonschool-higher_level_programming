#!/usr/bin/python3
"""Module task_05_basic_security: Define API security and Authentification techniques"""


from flask import Flask, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import get_jwt_identity


app = Flask(__name__)
auth =

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password1"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("adminpassword"),
        "role": "admin"
    }
}

