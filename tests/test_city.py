import unittest
from datetime import datetime
from unittest.mock import MagicMock

from models.base_model import BaseModel
from models.city import City
from models.country import Country


class TestCity(unittest.TestCase):

    def setUp(self):
        self.country = Country(name="Test Country")
        self.city = City(name="Test City", country=self.country)

    def test_city_creation(self):
        self.assertEqual(self.city.name, "Test City")
        self.assertEqual(self.city.country_id, self.country.id)
        self.assertEqual(self.city.country, self.country)
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertEqual(self.city.places, [])

    def test_add_place(self):
        place = MagicMock()
        place.id = "123"
        self.city.add_place(place)
        self.assertIn(place, self.city.places)
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_add_place_already_exists(self):
        place = MagicMock()
        place.id = "123"
        self.city.add_place(place)
        self.city.add_place(place)  # Adding the same place again
        self.assertEqual(len(self.city.places), 1)  # Ensure no duplicate

    def test_to_dict(self):
        place = MagicMock()
        place.id = "123"
        self.city.add_place(place)
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['name'], "Test City")
        self.assertEqual(city_dict['country_id'], self.country.id)
        self.assertEqual(city_dict['places'], ["123"])

    def test_from_dict(self):
        city_dict = {
            'id': self.city.id,
            'name': "Test City",
            'country_id': self.country.id,
            'created_at': self.city.created_at.isoformat(),
            'updated_at': self.city.updated_at.isoformat(),
            'places': []
        }
        new_city = City.from_dict(city_dict, self.country)
        self.assertEqual(new_city.id, self.city.id)
        self.assertEqual(new_city.name, "Test City")
        self.assertEqual(new_city.country_id, self.country.id)
        self.assertEqual(new_city.places, [])

    def test_to_json(self):
        place = MagicMock()
        place.id = "123"
        self.city.add_place(place)
        city_json = self.city.to_json()
        self.assertIsInstance(city_json, str)
        self.assertIn('"name": "Test City"', city_json)
        self.assertIn('"places": ["123"]', city_json)

    def test_from_json(self):
        city_dict = {
            'id': self.city.id,
            'name': "Test City",
            'country_id': self.country.id,
            'created_at': self.city.created_at.isoformat(),
            'updated_at': self.city.updated_at.isoformat(),
            'places': []
        }
        city_json = json.dumps(city_dict)
        new_city = City.from_json(city_json, self.country)
        self.assertEqual(new_city.id, self.city.id)
        self.assertEqual(new_city.name, "Test City")
        self.assertEqual(new_city.country_id, self.country.id)
        self.assertEqual(new_city.places, [])

    def test_save_to_json(self):
        place = MagicMock()
        place.id = "123"
        self.city.add_place(place)
        filename = 'test_city.json'
        self.city.save_to_json(filename)
        with open(filename, 'r') as file:
            data = json.load(file)
        self.assertEqual(data['name'], "Test City")
        self.assertEqual(data['country_id'], self.country.id)
        self.assertEqual(data['places'], ["123"])
        import os
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()
