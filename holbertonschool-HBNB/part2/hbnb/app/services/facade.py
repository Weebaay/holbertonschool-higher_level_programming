from app.persistence.repository import InMemoryRepository
from app.models.user import User


class HBnBFacade:
    def __init__(self):
        """
        Initializes the HBnBFacade with an in-memory repository for users.
        """
        self.user_repo = InMemoryRepository()

    def create_user(self, user_data):
        """
        Creates a new user and adds them to the repository.
        
        Args:
            user_data (dict): Dictionary containing user attributes (first_name, last_name, email).
        
        Returns:
            User: The created user object.
        """
        # Creating a new user from the provided data
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """
        Retrieves a user by their ID.
        
        Args:
            user_id (str): The unique identifier of the user.
        
        Returns:
            User: The user object if found, or None if not found.
        """
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """
        Retrieves a user by their email.
        
        Args:
            email (str): The email address of the user.
        
        Returns:
            User: The user object if found, or None if not found.
        """
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, user_data):
        """
        Updates the details of an existing user.
        
        Args:
            user_id (str): The unique identifier of the user to update.
            user_data (dict): Dictionary containing the updated user attributes.
        
        Returns:
            User: The updated user object if found, or None if the user does not exist.
        """
        # Retrieve the user by ID
        user = self.get_user(user_id)
        if user:
            # Update the user with the provided data
            self.user_repo.update(user_id, user_data)
            return user
        return None
