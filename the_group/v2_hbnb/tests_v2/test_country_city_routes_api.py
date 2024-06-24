import unittest
import json
import sys
import os

# Ensure the app module can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api import app

class TestCountryCityRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_city(self):
        payload = {
            'name': 'Test City',
            'country_code': 'US'
        }
        response = self.app.post('/cities', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_create_city_missing_fields(self):
        payload = {
            'name': 'Test City'
            # 'country_code' is missing
        }
        response = self.app.post('/cities', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_get_countries(self):
        response = self.app.get('/countries')
        self.assertEqual(response.status_code, 200)

    def test_get_country(self):
        response = self.app.get('/countries/US')
        self.assertIn(response.status_code, [200, 404])

    def test_get_cities_by_country(self):
        response = self.app.get('/countries/US/cities')
        self.assertEqual(response.status_code, 200)

    def test_get_cities(self):
        response = self.app.get('/cities')
        self.assertEqual(response.status_code, 200)

    def test_get_city(self):
        response = self.app.get('/cities/1')
        self.assertIn(response.status_code, [200, 404])

    def test_update_city(self):
        payload = {
            'name': 'Updated City'
        }
        response = self.app.put('/cities/1', data=json.dumps(payload), content_type='application/json')
        self.assertIn(response.status_code, [200, 404])

    def test_delete_city(self):
        response = self.app.delete('/cities/1')
        self.assertIn(response.status_code, [204, 404])

if __name__ == '__main__':
    unittest.main()
