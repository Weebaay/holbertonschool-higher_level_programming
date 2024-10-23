
class InMemoryRepository:
    def __init__(self):
        """Initializes an empty storage dictionary."""
        self.storage = {}

    def add(self, obj):
        """Adds an object to the repository."""
        self.storage[obj.id] = obj

    def get(self, obj_id):
        """Retrieves an object by its ID."""
        return self.storage.get(obj_id)

    def get_all(self):
        """Retrieves all objects from the repository."""
        return list(self.storage.values())

    def update(self, obj_id, data):
        """Updates an object in the repository."""
        obj = self.get(obj_id)
        if obj:
            obj.update(data)

    def delete(self, obj_id):
        """Deletes an object by its ID."""
        if obj_id in self.storage:
            del self.storage[obj_id]

    def get_by_attribute(self, attr_name, attr_value):
        """Retrieves an object by one of its attributes."""
        return next((obj for obj in self.storage.values() if getattr(obj, attr_name) == attr_value), None)
