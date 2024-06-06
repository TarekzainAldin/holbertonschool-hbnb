import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def test_place_creation(self):
        place = Place("Test Place", "A test description", "123 Test St", "1", 10.0, 10.0, "1", 3, 2, 100, 4, ["WiFi"])
        self.assertEqual(place.name, "Test Place")
        self.assertEqual(place.address, "123 Test St")

if __name__ == '__main__':
    unittest.main()
