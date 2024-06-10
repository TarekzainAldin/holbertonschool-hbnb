# tests/test_user_endpoints.py

import unittest
from models.user import User  # Import the User class
from persistence.data_manager import DataManager

class TestDataPersistence(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()

    def test_save_and_retrieve_user(self):
        user = User(email="test@example.com", first_name="John", last_name="Doe")
        saved_user = self.data_manager.save(user)
        self.assertIsNotNone(saved_user)
        retrieved_user = self.data_manager.get(saved_user['id'], 'User')
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, "test@example.com")

    def test_update_user(self):
        user = User(email="test@example.com", first_name="John", last_name="Doe")
        saved_user = self.data_manager.save(user)
        user.first_name = "Jane"
        self.data_manager.update(user)
        updated_user = self.data_manager.get(saved_user['id'], 'User')
        self.assertEqual(updated_user.first_name, "Jane")

    def test_delete_user(self):
        user = User(email="test@example.com", first_name="John", last_name="Doe")
        saved_user = self.data_manager.save(user)
        self.data_manager.delete(saved_user['id'], 'User')
        deleted_user = self.data_manager.get(saved_user['id'], 'User')
        self.assertIsNone(deleted_user)

if __name__ == '__main__':
    unittest.main()
