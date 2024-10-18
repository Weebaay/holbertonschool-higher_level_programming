#!/usr/bin/python3
"""Module task_05_basic_security: Define API security and
Authentication techniques"""

from functools import wraps
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

# Configuration pour JWT
# Utilise une clé secrète forte ici
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# Base de données utilisateurs stockée en mémoire
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),  # Hash du mot de passe
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),  # Hash du mot de passe
        "role": "admin"
    }
}

# Vérification de mot de passe pour Basic Authentication


@auth.verify_password
def verify_password(username, password):
    """
    Vérifie les identifiants pour l'authentification basique.
    Retourne le nom d'utilisateur si les identifiants sont valides, sinon None.
    """
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username  # Renvoie le nom d'utilisateur si authentification réussie
    return None

# Gestionnaire d'erreurs pour Basic Auth


@auth.error_handler
def auth_error(status):
    """
    Gère les erreurs d'authentification Basic.
    Retourne une réponse 401 Unauthorized si l'authentification échoue.
    """
    return jsonify({"error": "Unauthorized access"}), 401

# Route protégée par Basic Auth


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    Route protégée par l'authentification basique.
    Retourne un message si les identifiants sont valides.
    """
    return "Basic Auth: Access Granted"

# Route pour se connecter et obtenir un token JWT


@app.route('/login', methods=['POST'])
def login():
    """
    Route de connexion pour obtenir un jeton JWT.
    Exige un nom d'utilisateur et un mot de passe, renvoie un JWT si les identifiants sont valides.
    """
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password are required"}), 400

    username = data.get('username')
    password = data.get('password')
    user = users.get(username)

    if user and check_password_hash(user['password'], password):
        # Génère un token JWT avec les informations de l'utilisateur (username, role)
        access_token = create_access_token(
            identity={'username': username, 'role': user['role']})
        return jsonify(access_token=access_token)
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# Route protégée par JWT


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    Route protégée par JWT.
    Retourne un message si le token JWT est valide.
    """
    current_user = get_jwt_identity()
    return jsonify({"message": "JWT Auth: Access Granted", "user": current_user})

# Décorateur pour vérifier si l'utilisateur a le rôle d'administrateur


def admin_required(fn):
    """
    Décorateur pour vérifier si l'utilisateur a le rôle d'admin.
    Renvoie un message d'erreur si l'utilisateur n'est pas un administrateur.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        jwt_identity = get_jwt_identity()
        if jwt_identity and jwt_identity.get('role') == 'admin':
            return fn(*args, **kwargs)
        else:
            return jsonify({"error": "Admin access required"}), 403
    return wrapper

# Route accessible uniquement par les administrateurs


@app.route('/admin-only', methods=['GET'])
@jwt_required()
@admin_required
def admin_only():
    """
    Route protégée accessible uniquement aux administrateurs.
    Retourne un message si l'utilisateur est un administrateur.
    """
    return "Admin Access: Granted"

# Gestionnaire d'erreurs JWT pour token manquant ou invalide


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Gère les erreurs d'authentification JWT lorsque le token est manquant ou invalide.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Gère les erreurs d'authentification JWT lorsque le token est invalide.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Gère les erreurs d'authentification JWT lorsque le token a expiré.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Gère les erreurs d'authentification JWT lorsque le token a été révoqué.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Gère les erreurs d'authentification JWT lorsque le token fraîchement émis est requis.
    """
    return jsonify({"error": "Fresh token required"}), 401


# Lancement de l'application Flask
if __name__ == '__main__':
    app.run(debug=True)
