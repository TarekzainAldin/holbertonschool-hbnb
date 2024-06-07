import unittest
from unittest.mock import patch
from models.city  import City

class TestCity(unittest.TestCase):
    @patch('city.json.load')
    def test_city_creation(self, mock_json_load):
        # Mock the json.load function to return sample JSON data
        mock_json_load.return_value = {
            "id": "1",
            "name": "New York",
            "country_id": "country1",
            "created_at": "2024-06-07T12:00:00",
            "updated_at": "2024-06-07T12:00:00",
            "places": []
        }

        # Create a city object for testing
        city = City.from_json("test_city.json")

        # Check if the city object is created correctly
        self.assertEqual(city.name, "New York")
        self.assertEqual(city.country_id, "country1")

    @patch('city.json.dump')
    def test_save_to_json(self, mock_json_dump):
        # Create a city object for testing
        city = City(name="Test City", country_id="country1")

        # Save the city object to a JSON file
        city.save_to_json("test_city.json")

        # Check if the json.dump function is called with the expected arguments
        mock_json_dump.assert_called_once_with({
            "id": city.id,
            "name": "Test City",
            "country_id": "country1",
            "created_at": city.created_at.isoformat(),
            "updated_at": city.updated_at.isoformat(),
            "places": []
        }, "test_city.json")

if __name__ == "__main__":
    unittest.main()
