from persistence.IPersistenceManager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self):
        self.data = {}  # Data storage dictionary

    def save(self, entity):
        entity_id = entity.email  # Assuming email as the unique identifier
        self.data[entity_id] = entity

    def get(self, entity_id, entity_type):
        return self.data.get(entity_id)

    def update(self, entity):
        # Update the entity if it exists in the data storage
        entity_id = entity.email
        if entity_id in self.data:
            self.data[entity_id] = entity
        else:
            raise ValueError(f"Entity with ID '{entity_id}' does not exist.")

    def delete(self, entity_id, entity_type):
        if entity_id in self.data:
            del self.data[entity_id]
        else:
            raise ValueError(f"Entity with ID '{entity_id}' does not exist.")
