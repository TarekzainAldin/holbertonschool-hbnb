import unittest
from datetime import datetime
from models.user import User
from persistence.data_manager import DataManager

class TestDataPersistence(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()

    def test_save_and_get(self):
        # Create a user
        user = User(email="alice@example.com", first_name="Alice", last_name="Smith")
        saved_id = self.data_manager.save(user)['id']

        # Retrieve the user by ID
        retrieved_user = self.data_manager.get(saved_id, "User")

        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, "alice@example.com")
        self.assertEqual(retrieved_user.first_name, "Alice")
        self.assertEqual(retrieved_user.last_name, "Smith")

    def test_update(self):
        # Create a user
        user = User(email="bob@example.com", first_name="Bob", last_name="Johnson")
        saved_id = self.data_manager.save(user)['id']

        # Retrieve the user by ID
        updated_user = User(email="bob.updated@example.com", first_name="Bob Updated", last_name="Johnson")
        # Manually set the ID for updated_user
        setattr(updated_user, 'id', saved_id)

        self.assertTrue(self.data_manager.update(updated_user))

        # Retrieve the user again and check if it's updated
        retrieved_user = self.data_manager.get(saved_id, "User")
        self.assertEqual(retrieved_user.email, "bob.updated@example.com")
        self.assertEqual(retrieved_user.first_name, "Bob Updated")

    def test_delete(self):
        # Create a user
        user = User(email="charlie@example.com", first_name="Charlie", last_name="Brown")
        saved_id = self.data_manager.save(user)['id']

        # Delete the user
        self.assertTrue(self.data_manager.delete(saved_id, "User"))

        # Try to retrieve the deleted user
        retrieved_user = self.data_manager.get(saved_id, "User")
        self.assertIsNone(retrieved_user)

if __name__ == '__main__':
    unittest.main()
