# persistence/amenity_data_manager.py

from persistence.IPersistenceManager import IPersistenceManager
from models.amenity import Amenity

class AmenityDataManager(IPersistenceManager):
    def __init__(self):
        self.data = {}

    def save(self, entity):
        if not isinstance(entity, Amenity):
            return {'error': 'Invalid entity type'}
        entity_type = type(entity).__name__
        if entity_type not in self.data:
            self.data[entity_type] = []
        entity_id = len(self.data[entity_type]) + 1
        setattr(entity, 'id', entity_id)
        self.data[entity_type].append(entity)
        return {'id': entity_id}

    def get(self, entity_id):
        if 'Amenity' in self.data:
            for entity in self.data['Amenity']:
                if getattr(entity, 'id', None) == entity_id:
                    return entity
        return None

    def update(self, entity):
        if not isinstance(entity, Amenity):
            return False
        if 'Amenity' in self.data:
            for idx, e in enumerate(self.data['Amenity']):
                if getattr(e, 'id', None) == getattr(entity, 'id', None):
                    self.data['Amenity'][idx] = entity
                    return True
        return False

    def delete(self, entity_id):
        if 'Amenity' in self.data:
            for idx, entity in enumerate(self.data['Amenity']):
                if getattr(entity, 'id', None) == entity_id:
                    del self.data['Amenity'][idx]
                    return True
        return False

    def get_all(self):
        return self.data.get('Amenity', [])

    def exists(self, name):
        if 'Amenity' in self.data:
            for entity in self.data['Amenity']:
                if entity.name == name:
                    return True
        return False

    def get_by_name(self, name):
        if 'Amenity' in self.data:
            for entity in self.data['Amenity']:
                if entity.name == name:
                    return entity
        return None
