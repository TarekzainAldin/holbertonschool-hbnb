import unittest
import json
from api.app import app
class TestCountryCityEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    def test_get_countries(self):
        response = self.app.get('/countries')
        self.assertEqual(response.status_code, 200)
        countries = json.loads(response.data)
        self.assertGreater(len(countries), 0)
    def test_get_country(self):
        response = self.app.get('/countries/US')
        self.assertEqual(response.status_code, 200)
        country = json.loads(response.data)
        self.assertEqual(country['code'], 'US')
    def test_get_country_not_found(self):
        response = self.app.get('/countries/ZZ')
        self.assertEqual(response.status_code, 404)
    def test_create_city(self):
        response = self.app.post('/cities', json={
            'name': 'New York',
            'country_code': 'US'
        })
        self.assertEqual(response.status_code, 201)
        city = json.loads(response.data)
        self.assertEqual(city['name'], 'New York')
    def test_get_city(self):
        response = self.app.post('/cities', json={
            'name': 'Los Angeles',
            'country_code': 'US'
        })
        city_id = json.loads(response.data)['id']
        response = self.app.get(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 200)
        city = json.loads(response.data)
        self.assertEqual(city['name'], 'Los Angeles')
    def test_update_city(self):
        response = self.app.post('/cities', json={
            'name': 'Chicago',
            'country_code': 'US'
        })
        city_id = json.loads(response.data)['id']
        response = self.app.put(f'/cities/{city_id}', json={
            'name': 'Chicago Updated',
            'country_code': 'US'
        })
        self.assertEqual(response.status_code, 200)
        city = json.loads(response.data)
        self.assertEqual(city['name'], 'Chicago Updated')
    def test_delete_city(self):
        response = self.app.post('/cities', json={
            'name': 'San Francisco',
            'country_code': 'US'
        })
        city_id = json.loads(response.data)['id']
        response = self.app.delete(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 204)
        response = self.app.get(f'/cities/{city_id}')
        self.assertEqual(response.status_code, 404)
if __name__ == '__main__':
    unittest.main()
