"""

This module defines the User class, which is used to represent
a user in the HBnB system. It includes attributes such as 
first_name, last_name, email, and password.
"""
from app.models.base_model import BaseModel


class User(BaseModel):
    """Represents a user in the HBnB system."""

    def __init__(self, first_name, last_name, email, password=None):
        """
        Initializes a new User instance.
        
        Args:
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            email (str): The user's email address.
            password (str): The user's password.
        """
        super().__init__()  # Appelle le constructeur de BaseModel
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = False  # Par défaut, l'utilisateur n'est pas admin
        self.password = password

    def to_dict(self):
        """
        Converts the User instance into a dictionary.

        Returns:
            dict: A dictionary containing the user's details.
        """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
