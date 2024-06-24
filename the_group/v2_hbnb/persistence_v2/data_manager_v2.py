# persistence/data_manager.py

from models.user import User
from persistence.IPersistenceManager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self):
        self.data = {}  # Dictionary to store data by entity type

    def save(self, entity):
        """
        Save an entity.
        """
        entity_type = type(entity).__name__
        if entity_type not in self.data:
            self.data[entity_type] = []

        entity_id = len(self.data[entity_type]) + 1
        setattr(entity, 'id', entity_id)
        self.data[entity_type].append(entity)
        return {'id': entity_id}

    def get(self, entity_id, entity_type):
        """
        Get an entity by ID.
        """
        if entity_type in self.data:
            for entity in self.data[entity_type]:
                if getattr(entity, 'id', None) == entity_id:
                    return entity
        return None

    def update(self, entity):
        """
        Update an entity.
        """
        entity_type = type(entity).__name__
        if entity_type in self.data:
            for idx, e in enumerate(self.data[entity_type]):
                if getattr(e, 'id', None) == getattr(entity, 'id', None):
                    self.data[entity_type][idx] = entity
                    return True
        return False

    def delete(self, entity_id, entity_type):
        """
        Delete an entity by ID.
        """
        if entity_type in self.data:
            for idx, entity in enumerate(self.data[entity_type]):
                if getattr(entity, 'id', None) == entity_id:
                    del self.data[entity_type][idx]
                    return True
        return False
