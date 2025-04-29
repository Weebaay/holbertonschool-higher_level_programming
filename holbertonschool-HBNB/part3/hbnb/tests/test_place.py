

import unittest
from app.models.place import Place
from app.models.user import User
from app.models.review import Review
from app.models.amenity import Amenity


class TestPlace(unittest.TestCase):
    """Test case for the Place class."""

    def test_place_creation(self):
        """Test that a Place instance is created with the correct attributes."""
        owner = User(first_name="Alice", last_name="Smith",
                     email="alice.smith@example.com", password="password123")
        place = Place(title="Lovely Apartment", description="A cozy place to stay",
                      price=100.0, latitude=40.7128, longitude=-74.0060, owner=owner)

        self.assertEqual(place.title, "Lovely Apartment")
        self.assertEqual(place.description, "A cozy place to stay")
        self.assertEqual(place.price, 100.0)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        # Vérifie la relation avec le propriétaire
        self.assertEqual(place.owner.first_name, "Alice")

    def test_add_review_to_place(self):
        """Test adding a review to a place."""
        owner = User(first_name="Alice", last_name="Smith",
                     email="alice.smith@example.com", password="password123")
        place = Place(title="Lovely Apartment", description="A cozy place to stay",
                      price=100.0, latitude=40.7128, longitude=-74.0060, owner=owner)
        review = Review(text="Great stay!", rating=5, place=place, user=owner)

        place.add_review(review)

        self.assertEqual(len(place.reviews), 1)
        self.assertEqual(place.reviews[0].text, "Great stay!")

    def test_add_amenity_to_place(self):
        """Test adding an amenity to a place."""
        owner = User(first_name="Alice", last_name="Smith",
                     email="alice.smith@example.com", password="password123")
        place = Place(title="Lovely Apartment", description="A cozy place to stay",
                      price=100.0, latitude=40.7128, longitude=-74.0060, owner=owner)
        amenity = Amenity(name="Wi-Fi")

        place.add_amenity(amenity)

        self.assertEqual(len(place.amenities), 1)
        self.assertEqual(place.amenities[0].name, "Wi-Fi")


if __name__ == '__main__':
    unittest.main()
