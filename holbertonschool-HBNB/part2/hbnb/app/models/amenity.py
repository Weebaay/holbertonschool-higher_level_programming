
from app.models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity in the HBnB system."""

    def __init__(self, name):
        """
        Initializes a new Amenity instance.

        Args:
            name (str): The name of the amenity (e.g., Wi-Fi, Parking).
        """
        super().__init__()  # Appelle le constructeur de BaseModel
        self.name = name

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
