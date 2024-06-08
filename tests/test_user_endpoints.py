import unittest
import json
from api.app import create_app
from persistence.data_manager import DataManager

class TestUserEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.data_manager = DataManager()

    def tearDown(self):
        # Clear the data after each test
        self.data_manager.data.clear()
    

    def test_create_user(self):
        # Test creating a user
        user_data = {
            "email": "test@example.com",
            "first_name": "John",
            "last_name": "Doe"
        }
        response = self.app.post('/users', json=user_data)
        self.assertEqual(response.status_code, 201)

        # Check if user was created correctly
        data = json.loads(response.data)
        self.assertEqual(data['message'], "User created successfully")
        self.assertEqual(data['user']['email'], "test@example.com")

    def test_get_user(self):
        # Add a user for testing
        user_id = self.data_manager.save({"email": "test@example.com", "first_name": "John", "last_name": "Doe"})['email']

        response = self.app.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['email'], "test@example.com")

    def test_get_users(self):
        # Add some users for testing
        self.data_manager.save({"email": "test1@example.com", "first_name": "Alice", "last_name": "Smith"})
        self.data_manager.save({"email": "test2@example.com", "first_name": "Bob", "last_name": "Johnson"})

        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data['users']), 2)

if __name__ == '__main__':
    unittest.main()


    def test_delete_user(self):
        # Test deleting a user
        # Create a user
        self.app.post('/users', json={"email": "test@example.com", "first_name": "John", "last_name": "Doe"})
        
        # Delete the user
        response = self.app.delete('/users/1')  # Assuming the ID is 1
        self.assertEqual(response.status_code, 204)

        # Check if user is deleted
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
