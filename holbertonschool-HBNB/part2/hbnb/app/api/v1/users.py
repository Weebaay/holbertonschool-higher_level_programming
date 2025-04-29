# app/api/v1/users.py
from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade
from app.models.user import User

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(
        required=True, description='First name of the user'),
    'last_name': fields.String(
        required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(
        required=True, description='Password of the user')
})

facade = HBnBFacade()


@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered or invalid data')
    def post(self):
        """Register a new user"""
        user_data = api.payload
        print(f"Received payload: {user_data}")

        # Check if the email is already registered
        existing_user = facade.get_user_by_email(
            user_data['email'].strip().lower())
        if existing_user:
            print(f"Email already registered: {user_data['email']}")
            return {'error': 'Email already registered'}, 400

        # Create the new user and hash the password
        try:
            new_user = User(
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                email=user_data['email'].strip().lower()
            )
            new_user.hash_password(user_data['password'])
            facade.user_repo.add(new_user)

            print(f"User created: {new_user.__dict__}")  # Log temporaire
            return {
                'id': new_user.id,
                'first_name': new_user.first_name,
                'last_name': new_user.last_name,
                'email': new_user.email
            }, 201
        except Exception as e:
            print(f"Error while creating user: {e}")
            return {'error': 'Failed to create user'}, 500

    @api.response(200, 'Users successfully retrieved')
    def get(self):
        """Retrieve the list of all users."""
        users = facade.user_repo.get_all()
        return [
            {
                'id': u.id,
                'first_name': u.first_name,
                'last_name': u.last_name,
                'email': u.email
            }
            for u in users
        ], 200


@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200

    @api.expect(user_model, validate=True)
    @api.response(200, 'User successfully updated')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    def put(self, user_id):
        """Update user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        user_data = api.payload
        print(f"Updating user with data: {user_data}")  # Log temporaire

        # Update user details
        try:
            user.update(user_data)
            return {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            }, 200
        except Exception as e:
            print(f"Error while updating user: {e}")  # Log temporaire
            return {'error': 'Failed to update user'}, 500