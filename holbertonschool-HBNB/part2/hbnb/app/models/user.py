from app.models.base_model import BaseModel


class User(BaseModel):
    """Represents a user in the HBnB system."""

    def __init__(self, first_name, last_name, email, password=None):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = False
        self.password = password

    @staticmethod
    def validate_first_name(first_name):
        if not first_name:
            raise ValueError("First name cannot be empty")

    @staticmethod
    def validate_last_name(last_name):
        if not last_name:
            raise ValueError("Last name cannot be empty")

    @staticmethod
    def validate_email(email):
        if not email or "@" not in email:
            raise ValueError("Invalid email format")

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
