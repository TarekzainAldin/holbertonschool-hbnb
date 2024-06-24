from persistence.IPersistenceManager import IPersistenceManager
from models.city import City

class CityDataManager(IPersistenceManager):
    def __init__(self, countries):
        self.data = {}
        self.countries = {country.code: country for country in countries}

    def save(self, entity):
        if not isinstance(entity, City):
            return {'error': 'Invalid entity type'}
        if entity.country_code not in self.countries:
            return {'error': 'Invalid country code'}
        entity_type = type(entity).__name__
        if entity_type not in self.data:
            self.data[entity_type] = []
        entity_id = len(self.data[entity_type]) + 1
        setattr(entity, 'id', entity_id)
        self.data[entity_type].append(entity)
        return {'id': entity_id}

    def get(self, entity_id):
        if 'City' in self.data:
            for entity in self.data['City']:
                if getattr(entity, 'id', None) == entity_id:
                    return entity
        return None

    def update(self, entity):
        if not isinstance(entity, City):
            return False
        if 'City' in self.data:
            for idx, e in enumerate(self.data['City']):
                if getattr(e, 'id', None) == getattr(entity, 'id', None):
                    self.data['City'][idx] = entity
                    return True
        return False

    def delete(self, entity_id):
        if 'City' in self.data:
            for idx, entity in enumerate(self.data['City']):
                if getattr(entity, 'id', None) == entity_id:
                    del self.data['City'][idx]
                    return True
        return False

    def get_all(self):
        return self.data.get('City', [])

    def get_by_country(self, country_code):
        if 'City' in self.data:
            return [city for city in self.data['City'] if city.country_code == country_code]
        return []
