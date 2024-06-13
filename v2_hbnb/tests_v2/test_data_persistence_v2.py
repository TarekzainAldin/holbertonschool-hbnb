import unittest
from models.user import User
from persistence.data_manager import DataManager

class TestDataPersistence(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()

    def test_save_and_retrieve_entity(self):
        # Create an entity
        entity_attributes = {'email': 'test@example.com', 'first_name': 'John', 'last_name': 'Doe'}
        entity_id = self.data_manager.save('User', **entity_attributes)['id']

        # Retrieve the entity
        retrieved_entity = self.data_manager.get(entity_id, 'User')

        # Check if entity is retrieved successfully
        self.assertIsNotNone(retrieved_entity)
        self.assertEqual(retrieved_entity.email, entity_attributes['email'])

    def test_update_entity(self):
        # Create an entity
        entity_attributes = {'email': 'test@example.com', 'first_name': 'John', 'last_name': 'Doe'}
        entity_id = self.data_manager.save('User', **entity_attributes)['id']

        # Update the entity
        updated_attributes = {'email': 'updated@example.com', 'first_name': 'Jane', 'last_name': 'Smith'}
        updated_entity = User(**updated_attributes)
        updated_entity.id = entity_id
        self.data_manager.update(updated_entity)

        # Retrieve the updated entity
        retrieved_entity = self.data_manager.get(entity_id, 'User')

        # Check if entity is updated successfully
        self.assertIsNotNone(retrieved_entity)
        self.assertEqual(retrieved_entity.email, updated_attributes['email'])
        self.assertEqual(retrieved_entity.first_name, updated_attributes['first_name'])
        self.assertEqual(retrieved_entity.last_name, updated_attributes['last_name'])

    def test_delete_entity(self):
        # Create an entity
        entity_attributes = {'email': 'test@example.com', 'first_name': 'John', 'last_name': 'Doe'}
        entity_id = self.data_manager.save('User', **entity_attributes)['id']

        # Delete the entity
        self.assertTrue(self.data_manager.delete(entity_id, 'User'))

        # Ensure the entity is deleted
        self.assertIsNone(self.data_manager.get(entity_id, 'User'))

if __name__ == '__main__':
    unittest.main()
