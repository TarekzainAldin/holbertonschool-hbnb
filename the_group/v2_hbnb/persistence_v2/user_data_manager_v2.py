from persistence.IPersistenceManager import IPersistenceManager
from models.user import User

class UserDataManager(IPersistenceManager):
    def __init__(self):
        self.data = []

    def save(self, entity):
        if not isinstance(entity, User):
            return {'error': 'Invalid entity type'}
        entity.id = len(self.data) + 1
        self.data.append(entity)
        return entity.to_dict()

    def get(self, entity_id):
        for entity in self.data:
            if entity.id == entity_id:
                return entity
        return None

    def update(self, entity):
        if not isinstance(entity, User):
            return False
        for idx, e in enumerate(self.data):
            if e.id == entity.id:
                self.data[idx] = entity
                return True
        return False

    def delete(self, entity_id):
        for idx, entity in enumerate(self.data):
            if entity.id == entity_id:
                del self.data[idx]
                return True
        return False

    def get_all(self):
        return self.data
