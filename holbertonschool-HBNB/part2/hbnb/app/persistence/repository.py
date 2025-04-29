# app/persistence/repository.py
from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository(Repository):
    def __init__(self):
        self._storage = {}
        self._index = {}

    def add(self, obj):
        self._storage[obj.id] = obj
        if hasattr(obj, 'email'):
            normalized_email = obj.email.strip().lower()
            self._index[normalized_email] = obj

    def get(self, obj_id):
        return self._storage.get(obj_id)

    def get_all(self):
        return list(self._storage.values())

    def get_by_attribute(self, attr_name, attr_value):
        normalized_value = attr_value.strip().lower()
        if attr_name == 'email':
            return self._index.get(normalized_value)
        else:
            for obj in self._storage.values():
                obj_value = getattr(obj, attr_name, None)
                if obj_value and obj_value.strip().lower() == normalized_value:
                    return obj
        return None

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)

    def delete(self, obj_id):
        if obj_id in self._storage:
            obj = self._storage.pop(obj_id)
            if hasattr(obj, 'email'):
                normalized_email = obj.email.strip().lower()
                self._index.pop(normalized_email, None)
