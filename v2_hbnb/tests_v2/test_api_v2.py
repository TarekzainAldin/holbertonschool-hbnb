import unittest
from flask import json
from api.app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_create_user(self):
        # Test creating a new user
        user_data = {"email": "test@example.com", "first_name": "Test", "last_name": "User"}
        response = self.app.post('/users', json=user_data)
        self.assertEqual(response.status_code, 201)

    def test_get_users(self):
        # Test retrieving all users
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        # Test retrieving a specific user
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        # Test updating a user
        user_data = {"email": "updated@example.com"}
        response = self.app.put('/users/1', json=user_data)
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        # Test deleting a user
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
