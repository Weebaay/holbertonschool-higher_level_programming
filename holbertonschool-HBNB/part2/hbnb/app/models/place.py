"""
Place model for the HBnB application.

This module defines the Place class, representing a property 
available for reservation in the HBnB system.
"""

from app.models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place (property) in the HBnB application."""

    def __init__(self, title, description, price, latitude, longitude, owner_id):
        """
        Initializes a new Place instance.

        Args:
            title (str): The title of the place.
            description (str): A detailed description of the place.
            price (float): The price per night.
            latitude (float): The latitude of the place's location.
            longitude (float): The longitude of the place's location.
            owner_id (str): The ID of the user who owns the place.
        """
        super().__init__()
        self.title = title
        self.description = description or ""
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id  # Changed to store only the owner ID
        self.reviews = []  # Store review objects
        self.amenities = []  # Store amenity objects

        # Perform validation when the object is created
        self.validate()

    def validate(self):
        """
        Validates the place's attributes.
        
        Raises:
            ValueError: If any of the validation checks fail.
        """
        if not self.title:
            raise ValueError("The title cannot be empty.")
        if self.price <= 0:
            raise ValueError("The price must be a positive number.")
        if not (-90 <= self.latitude <= 90):
            raise ValueError("The latitude must be between -90 and 90.")
        if not (-180 <= self.longitude <= 180):
            raise ValueError("The longitude must be between -180 and 180.")
        if not self.owner_id or not self.owner_id.strip():
            raise ValueError("The owner ID must be a valid non-empty string.")

    def add_amenity(self, amenity):
        """
        Adds an amenity to the list of amenities.
        
        Args:
            amenity: The amenity to add.
        """
        self.amenities.append(amenity)

    def add_review(self, review):
        """
        Adds a review to the list of reviews.
        
        Args:
            review: The review to add.
        """
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
            "owner_id": self.owner_id,
            "reviews": [review.to_dict() for review in self.reviews],
            "amenities": [amenity.to_dict() for amenity in self.amenities],
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
