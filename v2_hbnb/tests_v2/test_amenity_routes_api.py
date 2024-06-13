# tests/test_amenity_routes_api.py

import unittest
import json
import sys
import os

# Ensure the app module can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api import app

class TestAmenityRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_amenity(self):
        payload = {
            'name': 'WiFi'
        }
        response = self.app.post('/amenities', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_duplicate_amenity(self):
        payload = {
            'name': 'WiFi'
        }
        response = self.app.post('/amenities', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 409)

    def test_get_amenities(self):
        response = self.app.get('/amenities')
        self.assertEqual(response.status_code, 200)

    def test_get_amenity(self):
        response = self.app.get('/amenities/1')
        self.assertIn(response.status_code, [200, 404])

    def test_update_amenity(self):
        payload = {
            'name': 'Updated Amenity'
        }
        response = self.app.put('/amenities/1', data=json.dumps(payload), content_type='application/json')
        self.assertIn(response.status_code, [200, 404])

    def test_delete_amenity(self):
        response = self.app.delete('/amenities/1')
        self.assertIn(response.status_code, [204, 404])

if __name__ == '__main__':
    unittest.main()
