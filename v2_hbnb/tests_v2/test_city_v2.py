import json
import unittest
from datetime import datetime
from models.city import City
from models.country import Country


class TestCity(unittest.TestCase):
    def setUp(self):
        self.country = Country("USA")
        self.city = City("New York", self.country)

    def test_city_initialization(self):
        self.assertEqual(self.city.name, "New York")
        self.assertEqual(self.city.country_id, self.country.id)
        self.assertEqual(self.city.country, self.country)
        self.assertIsNotNone(self.city.created_at)
        self.assertIsNotNone(self.city.updated_at)
        self.assertEqual(len(self.city.places), 0)

    def test_add_place(self):
        place = "Central Park"
        self.city.add_place(place)
        self.assertEqual(len(self.city.places), 1)
        self.assertIn(place, self.city.places)

    def test_get_place(self):
        place = "Statue of Liberty"
        self.city.add_place(place)
        places = self.city.get_place()
        self.assertEqual(len(places), 1)
        self.assertEqual(places[0], place)

    def test_to_json(self):
        expected_json = {
            "id": self.city.id,
            "name": "New York",
            "country_id": self.country.id,
            "created_at": self.city.created_at.isoformat(),
            "updated_at": self.city.updated_at.isoformat(),
            "places": []
        }
        self.assertEqual(self.city.to_json(), expected_json)

    def test_from_json(self):
        json_data = {
            "id": "123",
            "name": "Los Angeles",
            "country_id": str(self.country.id),
            "created_at": "2024-06-10T12:00:00",
            "updated_at": "2024-06-10T12:00:00",
            "places": ["Hollywood Sign", "Santa Monica Pier"]
        }
        city = City.from_json(json.dumps(json_data))
        self.assertEqual(city.id, "123")
        self.assertEqual(city.name, "Los Angeles")
        self.assertEqual(city.country_id, self.country.id)
        self.assertEqual(city.created_at, datetime(2024, 6, 10, 12, 0, 0))
        self.assertEqual(city.updated_at, datetime(2024, 6, 10, 12, 0, 0))
        self.assertEqual(city.places, ["Hollywood Sign", "Santa Monica Pier"])

if __name__ == '__main__':
    unittest.main()
