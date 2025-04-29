import uuid
from app.models.base_model import BaseModel
from app.extension import bcrypt


class User(BaseModel):
    """Represents a user in the HBnB system."""

    def __init__(self, first_name, last_name, email, password=None):
        super().__init__()
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = False
        self.password = None
        if password:
            self.hash_password(password)
            
    def hash_password(self, password):
        """Hashes the password and stores it in the password attribute."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        if not self.password:
            return False  # Aucun mot de passe n'a été défini
        return bcrypt.check_password_hash(self.password, password)
    
    # def get_hashed_password(self):
    #   """Returns the hashed password (for debugging purposes only)."""
    #   return self.password 

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
