import unittest
import json
from api import app

class TestUserRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        payload = {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        }
        response = self.app.post('/api/v1/users', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_users(self):
        response = self.app.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        response = self.app.get('/api/v1/users/1')
        self.assertIn(response.status_code, [200, 404])

    def test_update_user(self):
        payload = {
            'first_name': 'Updated'
        }
        response = self.app.put('/api/v1/users/1', data=json.dumps(payload), content_type='application/json')
        self.assertIn(response.status_code, [200, 404])

    def test_delete_user(self):
        response = self.app.delete('/api/v1/users/1')
        self.assertIn(response.status_code, [204, 404])

if __name__ == '__main__':
    unittest.main()
