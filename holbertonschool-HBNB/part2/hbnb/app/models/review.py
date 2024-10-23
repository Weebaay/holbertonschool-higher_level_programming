"""
Review model for the HBnB application.

This module defines the Review class, representing a review left by 
a user for a particular place in the HBnB system.
"""
from app.models.base_model import BaseModel
from app.models.user import User
from app.models.place import Place


class Review(BaseModel):
    """Represents a review in the HBnB application."""

    def __init__(self, text, rating, place, user):
        """
        Initializes a new Review instance.

        Args:
            text (str): The content of the review.
            rating (int): The rating given to the place (1-5).
            place (Place): The place being reviewed.
            user (User): The user who wrote the review.
        """
        super().__init__()  # Appelle le constructeur de BaseModel
        self.text = text
        self.rating = rating
        self.place = place  # Référence vers un objet Place
        self.user = user  # Référence vers un objet User

    def to_dict(self):
        """
        Converts the Review instance into a dictionary.

        Returns:
            dict: A dictionary containing the review's details.
        """
        return {
            "id": self.id,
            "text": self.text,
            "rating": self.rating,
            "place": self.place.to_dict(),  # Inclure les détails du lieu
            "user": self.user.to_dict(),  # Inclure les détails de l'utilisateur
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
