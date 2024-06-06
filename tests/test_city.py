#!/usr/bin/python3
import unittest
import uuid
from models.city import City
from datetime import datetime

class TestCity(unittest.TestCase):
    def setUp(self):
        self.country_id = str(uuid.uuid4())
        self.city = City(name="Test City", country_id=self.country_id)

    def test_city_creation(self):
        self.assertEqual(self.city.name, "Test City")
        self.assertEqual(self.city.country_id, self.country_id)
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_city_operations(self):
        self.assertEqual(self.city.operation1("example"), str)
        # Add assertions based on the expected outcome of operation2

    def test_save_method(self):
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
