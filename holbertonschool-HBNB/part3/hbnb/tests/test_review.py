

import unittest
from app.models.review import Review
from app.models.user import User
from app.models.place import Place

class TestReview(unittest.TestCase):
    """Test case for the Review class."""

    def test_review_creation(self):
        """Test that a Review instance is created with the correct attributes."""
        user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="password123")
        place = Place(title="Charming Cottage", description="A beautiful place in the countryside", price=150.0, latitude=50.123, longitude=10.456, owner=user)
        review = Review(text="Amazing experience!", rating=5, place=place, user=user)

        self.assertEqual(review.text, "Amazing experience!")
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.place.title, "Charming Cottage")  # Vérifie la relation avec le lieu
        self.assertEqual(review.user.first_name, "John")  # Vérifie la relation avec l'utilisateur

if __name__ == '__main__':
    unittest.main()
