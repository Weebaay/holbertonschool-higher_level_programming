"""
This module defines the Review class, representing a review left by 
a user for a particular place in the HBnB system.
"""
from app.models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review in the HBnB application."""

    def __init__(self, text, rating, place_id, user_id):
        """
        Initializes a new Review instance.

        Args:
            text (str): The content of the review.
            rating (int): The rating given to the place (1-5).
            place_id (str): The ID of the place being reviewed.
            user_id (str): The ID of the user who wrote the review.
        """
        super().__init__()  # Call the constructor of BaseModel
        self.validate_text(text)
        self.validate_rating(rating)
        self.validate_user_id(user_id)
        self.validate_place_id(place_id)

        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

    def validate_text(self, text):
        """Validates that the review text is not empty."""
        if not text:
            raise ValueError("Review text cannot be empty")

    def validate_rating(self, rating):
        """Validates that the rating is between 1 and 5."""
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")

    def validate_user_id(self, user_id):
        """Validates that the user_id is not empty."""
        if not user_id:
            raise ValueError("User ID cannot be empty")

    def validate_place_id(self, place_id):
        """Validates that the place_id is not empty."""
        if not place_id:
            raise ValueError("Place ID cannot be empty")

    def to_dict(self):
        """Converts the Review instance into a dictionary."""
        return {
            "id": self.id,
            "text": self.text,
            "rating": self.rating,
            "place_id": self.place_id,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
