"""
Amenity model for the HBnB application.

This module defines the Amenity class, representing a service 
or facility available at a place in the HBnB system.
"""

from app.models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity in the HBnB application."""

    def __init__(self, name):
        """
        Initializes a new Amenity instance.

        Args:
            name (str): The name of the amenity.
        """
        super().__init__()
        self.name = name

        self.validate()

    def validate(self):
        """
        Validates the amenity's attributes.

        Raises:
            ValueError: If any of the validation checks fail.
        """
        if not self.name:
            raise ValueError("The name of the amenity cannot be empty.")

    def to_dict(self):
        """
        Converts the Amenity instance into a dictionary.

        Returns:
            dict: A dictionary containing the amenity's details.
        """
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
