import unittest
from models.amenitites import Amenity

class TestAmenity(unittest.TestCase):
    def test_amenity_creation(self):
        amenity = Amenity(name="Pool")
        self.assertIsInstance(amenity.id, str)
        self.assertEqual(amenity.name, "Pool")

if __name__ == "__main__":
    unittest.main()
