# tests/test_user_endpoints.py

import unittest
from models.user import User
from unittest.mock import patch
from flask import json
from api.app import app, data_manager  # Import your Flask app and data_manager

class TestUserEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        # Define a sample user data
        user_data = {
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        
        # Send a POST request to create a new user
        response = self.app.post('/users', json=user_data)

        # Assert the response status code
        self.assertEqual(response.status_code, 201)

        # Assert the response message and user data
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_data['message'], 'User created successfully')
        self.assertTrue('user' in response_data)
        self.assertEqual(response_data['user']['email'], user_data['email'])

    def test_get_user(self):
        # Create a new user to test retrieval
        new_user = data_manager.save_user(User('test@example.com', 'John', 'Doe'))

        # Send a GET request to retrieve the user
        response = self.app.get(f'/users/{new_user.id}')

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Assert the response user data
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_data['email'], new_user.email)

    # Add similar tests for other endpoints: update_user, delete_user, get_users

if __name__ == '__main__':
    unittest.main()
