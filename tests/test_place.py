#!/usr/bin/env python3
"""
This module contains classes representing the test for the place.
"""
import unittest
from models.place.py import Place
from models.user import User
from models.city import City

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place(
            id="1",
            name="Beautiful House",
            description="A nice place to stay",
            price=100.0,
            user_id="1",
            city_id="1"
        )

    def test_create_place(self):
        self.assertEqual(self.place.name, "Beautiful House")
        self.assertEqual(self.place.price, 100.0)
        self.assertEqual(self.place.user_id, "1")
        self.assertEqual(self.place.city_id, "1")

    def test_add_amenity(self):
        self.place.add_amenity("WiFi")
        self.assertIn("WiFi", self.place.amenities)

    def test_get_reviews(self):
        self.assertEqual(len(self.place.get_reviews()), 0)
        self.place.add_review("Great place!")
        self.assertEqual(len(self.place.get_reviews()), 1)

if __name__ == '__main__':
    unittest.main()
