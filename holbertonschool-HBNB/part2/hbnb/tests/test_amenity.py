
import unittest
from app.models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test case for the Amenity class."""

    def test_amenity_creation(self):
        """Test that an Amenity instance is created with the correct attributes."""
        amenity = Amenity(name="Wi-Fi")
        self.assertEqual(amenity.name, "Wi-Fi")
        self.assertIsNotNone(amenity.id)  # Vérifie que l'UUID est généré


if __name__ == '__main__':
    unittest.main()
