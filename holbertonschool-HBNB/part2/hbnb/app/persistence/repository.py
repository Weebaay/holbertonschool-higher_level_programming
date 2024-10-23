from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        """
        Adds a new object to the repository.
        """
        pass

    @abstractmethod
    def get(self, obj_id):
        """
        Retrieves an object by its ID from the repository.
        """
        pass

    @abstractmethod
    def get_all(self):
        """
        Retrieves all objects from the repository.
        """
        pass

    @abstractmethod
    def update(self, obj_id, data):
        """
        Updates an object in the repository by its ID.
        """
        pass

    @abstractmethod
    def delete(self, obj_id):
        """
        Deletes an object from the repository by its ID.
        """
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        """
        Retrieves an object from the repository by a specific attribute.
        """
        pass


class InMemoryRepository(Repository):
    def __init__(self):
        """
        Initializes the in-memory repository with an empty storage dictionary.
        """
        self._storage = {}

    def add(self, obj):
        """
        Adds a new object to the in-memory storage.
        Args:
            obj: The object to be added.
        """
        self._storage[obj.id] = obj

    def get(self, obj_id):
        """
        Retrieves an object by its ID from the in-memory storage.
        Args:
            obj_id (str): The unique identifier of the object.
        Returns:
            The object if found, or None if not found.
        """
        return self._storage.get(obj_id)

    def get_all(self):
        """
        Retrieves all objects from the in-memory storage.
        Returns:
            A list of all stored objects.
        """
        return list(self._storage.values())

    def update(self, obj_id, data):
        """
        Updates an existing object in the in-memory storage.
        Args:
            obj_id (str): The unique identifier of the object.
            data (dict): The data to update the object with.
        """
        obj = self.get(obj_id)
        if obj:
            obj.update(data)  # Calls the 'update' method of the object (assumes the object has an update method)

    def delete(self, obj_id):
        """
        Deletes an object from the in-memory storage by its ID.
        Args:
            obj_id (str): The unique identifier of the object.
        """
        if obj_id in self._storage:
            del self._storage[obj_id]

    def get_by_attribute(self, attr_name, attr_value):
        """
        Retrieves an object by a specific attribute from the in-memory storage.
        Args:
            attr_name (str): The name of the attribute to search by.
            attr_value: The value of the attribute to match.
        Returns:
            The first object that matches the attribute, or None if no match is found.
        """
        return next((obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value), None)
