from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.review import Review


class HBnBFacade:
    def __init__(self):
        """
        Initializes the HBnBFacade with an in-memory repository for users.
        """
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()

    def create_user(self, user_data):
        """
        Creates a new user and adds them to the repository.
        """
        try:
            user = User(**user_data)
            self.user_repo.add(user)
            return user
        except ValueError as e:
            raise ValueError(f"Invalid input data: {str(e)}")

    def get_user(self, user_id):
        """
        Retrieves a user by their ID.
        """
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """
        Retrieves a user by their email.
        """
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, user_data):
        """
        Updates the details of an existing user.
        """
        user = self.get_user(user_id)
        if user:
            self.user_repo.update(user_id, user_data)
            return user
        return None

    def create_amenity(self, amenity_data):
        """ Creates a new amenity and adds it to the repository."""

        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """Retrieves an amenity by its ID"""

        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        """Retrieves all amenities from the repository."""
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        """Updates the details of an existing amenity."""
        amenity = self.get_amenity(amenity_id)
        if amenity:
            self.amenity_repo.update(amenity_id, amenity_data)
            return amenity
        return None

    def create_review(self, review_data):
        """
        Creates a new review and adds it to the repository.
        Validates the user_id and place_id.
        """
        user = self.get_user(review_data['user_id'])
        if not user:
            raise ValueError(
                f"User ID {review_data['user_id']} does not exist.")
        place = self.place_repo.get(review_data['place_id'])
        if not place:
            raise ValueError(
                f"Place ID {review_data['place_id']} does not exist.")
        review = Review(
            text=review_data['text'],
            rating=review_data['rating'],
            place_id=review_data['place_id'],
            user_id=review_data['user_id']
        )
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        """Retrieves a review by its ID"""
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        """Retrieves all review from the repository"""
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        """Retrieves all reviews for a specific place by its ID"""
        return [r for r in self.review_repo.get_all()
                if r.place.id == place_id]

    def update_review(self, review_id, review_data):
        """Update an existing review's details"""
        review = self.get_review(review_id)
        if review:
            self.review_repo.update(review_id, review_data)
            return review
        return None

    def delete_review(self, review_id):
        """Delete a review by its Id"""
        review = self.get_review(review_id)
        if review:
            self.review_repo.delete(review_id)
            return True
        return False


facade = HBnBFacade()
