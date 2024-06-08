import unittest
from models.user import User
from persistence.data_manager import DataManager

class TestDataPersistence(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()

    def test_save_and_retrieve_user(self):
        # Create a user
        user = User(email="test@example.com", first_name="John", last_name="Doe")

        # Save the user
        self.data_manager.save(user)

        # Retrieve the user
        retrieved_user = self.data_manager.get(entity_id="test@example.com", entity_type="user")

        # Check if user is retrieved successfully
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(user.email, retrieved_user.email)

if __name__ == '__main__':
    unittest.main()
