"""
Place model for the HBnB application.

This module defines the Place class, representing a property 
available for reservation in the HBnB system.
"""

from app.models.base_model import BaseModel
from app.models.user import User


class Place(BaseModel):
    """Represents a place (property) in the HBnB application."""

    def __init__(self, title, description, price, latitude, longitude, owner):
        """
        Initializes a new Place instance.

        Args:
            title (str): The title of the place.
            description (str): A detailed description of the place.
            price (float): The price per night.
            latitude (float): The latitude of the place's location.
            longitude (float): The longitude of the place's location.
            owner (User): The user who owns the place.
        """
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []

    def add_amenity(self, amenity):
        """Adds convenience to the list of conveniences"""
        self.amenities.append(amenity)

    def add_review(self, review):
        """add feedback at the list """
        self.reviews.append(review)

    def to_dict(self):
        """
        Converts the Place instance into a dictionary.

        Returns:
            dict: A dictionary containing the place's details.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner": self.owner.to_dict(),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
