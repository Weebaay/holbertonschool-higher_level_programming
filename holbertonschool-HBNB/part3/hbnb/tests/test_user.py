

import unittest
from app.models.user import User


class TestUser(unittest.TestCase):
    """Test case for the User class."""

    def test_user_creation(self):
        """Test that a User instance is created with the correct attributes."""
        user = User(first_name="John", last_name="Doe",
                    email="john.doe@example.com", password="password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "john.doe@example.com")
        self.assertFalse(user.is_admin)  # Par défaut, is_admin doit être False
        self.assertIsNotNone(user.id)  # Vérifie que l'UUID est généré
        # Vérifie que la date de création est définie
        self.assertIsNotNone(user.created_at)


if __name__ == '__main__':
    unittest.main()
