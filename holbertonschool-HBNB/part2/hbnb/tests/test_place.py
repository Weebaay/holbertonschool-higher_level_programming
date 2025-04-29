import unittest
from app import create_app
from flask_jwt_extended import create_access_token


class TestPlacesAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app("config.TestingConfig")
        self.client = self.app.test_client()
        self.token = create_access_token(identity={"id": "user_id_example", "is_admin": False})

    def test_create_place(self):
        place_data = {
            "title": "Cozy Apartment",
            "description": "A nice place to stay.",
            "price": 120.0,
            "latitude": 37.7749,
            "longitude": -122.4194
        }
        headers = {"Authorization": f"Bearer {self.token}"}
        response = self.client.post("/api/v1/places/", json=place_data, headers=headers)
        self.assertEqual(response.status_code, 201)
