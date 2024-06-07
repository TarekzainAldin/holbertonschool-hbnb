import unittest
import sys
import os
from app import app
from models.user import User
from persistence import FileStorage

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.storage = FileStorage()
        self.storage._save_data({})  # Clear storage before each test

    def test_create_user(self):
        response = self.app.post('/api/users/', json={
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('email', response.get_json())

    def test_get_user(self):
        user = User(email='test@example.com', first_name='Test', last_name='User')
        self.storage.save(user)
        response = self.app.get(f'/api/users/{user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['email'], 'test@example.com')

    def test_update_user(self):
        user = User(email='test@example.com', first_name='Test', last_name='User')
        self.storage.save(user)
        response = self.app.put(f'/api/users/{user.id}', json={
            'email': 'updated@example.com',
            'first_name': 'Updated',
            'last_name': 'User'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['email'], 'updated@example.com')

    def test_delete_user(self):
        user = User(email='test@example.com', first_name='Test', last_name='User')
        self.storage.save(user)
        response = self.app.delete(f'/api/users/{user.id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
