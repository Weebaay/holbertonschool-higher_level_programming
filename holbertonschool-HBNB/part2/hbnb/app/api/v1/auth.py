# app/api/v1/auth.py
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.services.facade import HBnBFacade

api = Namespace('auth', description='Authentication operations')
facade = HBnBFacade()

# Modèle pour valider les données d'entrée
login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})


@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Authentifie un utilisateur et retourne un token JWT"""
        credentials = api.payload
        print(f"Tentative de connexion avec email='{credentials['email']}'")  # Log initial

        # Normalisation de l'email
        email = credentials['email'].strip().lower()
        print(f"Email normalisé pour la recherche : '{email}'")  # Log normalisation

        # Recherche de l'utilisateur
        user = facade.get_user_by_email(email)
        if not user:
            print(f"Aucun utilisateur trouvé avec l'email : '{email}'")  # Log échec
            return {'error': 'Invalid credentials'}, 401

        # Vérification du mot de passe
        if not user.verify_password(credentials['password']):
            print(f"Échec de la vérification du mot de passe pour l'utilisateur : '{email}'")  # Log échec
            return {'error': 'Invalid credentials'}, 401

        # Génération du token JWT
        access_token = create_access_token(identity={'id': str(user.id), 'is_admin': user.is_admin})
        print(f"Authentification réussie pour l'utilisateur : '{email}'")  # Log succès
        return {'access_token': access_token}, 200
