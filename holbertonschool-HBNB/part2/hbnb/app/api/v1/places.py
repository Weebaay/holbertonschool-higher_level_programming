from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.facade import HBnBFacade

api = Namespace('places', description='Place operations')

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
})

facade = HBnBFacade()

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model, validate=True)
    @api.response(201, 'Place successfully created')
    @jwt_required()  # Authentication required
    def post(self):
        """Register a new place"""
        current_user_id = get_jwt_identity()  # Get authenticated user ID
        place_data = api.payload

        place_data['owner_id'] = current_user_id

        try:
            # Validate and create the place
            new_place = facade.create_place(place_data)
        except ValueError as e:
            return {'error': str(e)}, 400

        return {
            'id': new_place.id,
            'title': new_place.title,
            'description': new_place.description,
            'price': new_place.price,
            'latitude': new_place.latitude,
            'longitude': new_place.longitude,
            'owner_id': new_place.owner_id
        }, 201

    @api.response(200, 'Places successfully retrieved')
    def get(self):
        """Retrieve all places (publicly accessible)"""
        places = facade.place_repo.get_all()
        return [{'id': p.id,
                 'title': p.title,
                 'price': p.price,
                 'description': p.description}
                for p in places], 200


@api.route('/<string:place_id>')
class PlaceResource(Resource):
    @api.expect(place_model, validate=True)
    @api.response(200, 'Place successfully updated')
    @api.response(403, 'Unauthorized action')
    @api.response(404, 'Place not found')
    @jwt_required()  # Authentication required
    def put(self, place_id):
        """Update a specific place (requires authentication)"""
        current_user_id = get_jwt_identity()
        place = facade.get_place(place_id)

        if not place:
            return {'error': 'Place not found'}, 404
        if place.owner_id != current_user_id:
            return {'error': 'Unauthorized action'}, 403

        # Update the place details
        try:
            updated_place = facade.update_place(place_id, api.payload)
        except ValueError as e:
            return {'error': str(e)}, 400

        return {
            'id': updated_place.id,
            'message': 'Place updated successfully'
        }, 200
