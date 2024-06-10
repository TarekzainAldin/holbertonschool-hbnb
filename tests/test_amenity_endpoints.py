import unittest
from app import app, amenities

class AmenityTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        amenities.clear()

    def test_create_amenity(self):
        response = self.app.post('/amenities/', json={'name': 'Pool'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Pool', response.get_json()['name'])

    def test_get_amenity(self):
        self.app.post('/amenities/', json={'name': 'Gym'})
        response = self.app.get('/amenities/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Gym', response.get_json()['name'])

    # Add more tests for PUT, DELETE, and edge cases

if __name__ == '__main__':
    unittest.main()
