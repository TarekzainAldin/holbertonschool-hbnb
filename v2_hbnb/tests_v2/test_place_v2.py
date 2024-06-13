# tests/test_place.py
import unittest
from datetime import datetime
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_place_creation(self):
        place = Place("Cozy Apartment", "A lovely apartment", "123 Main St", "city_1", 40.7128, -74.0060,
                      "host@example.com", 2, 1, 100, 4)
        self.assertEqual(place.name, "Cozy Apartment")
        self.assertEqual(place.description, "A lovely apartment")
        self.assertEqual(place.city_id, "city_1")
        self.assertEqual(place.host_id, "host@example.com")
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)

    def test_add_amenity(self):
        place = Place("Cozy Apartment", "A lovely apartment", "123 Main St", "city_1", 40.7128, -74.0060,
                      "host@example.com", 2, 1, 100, 4)
        place.add_amenity("Wi-Fi")
        self.assertEqual(len(place.amenities), 1)
        self.assertEqual(place.amenities[0], "Wi-Fi")

    # Add more tests for other methods and business logic

if __name__ == '__main__':
    unittest.main()
