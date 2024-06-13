from models.city import City
from persistence.city_data_manager import CityDataManager
import unittest

class TestCityDataManager(unittest.TestCase):
    def setUp(self):
        # Initialize a CityDataManager instance for each test method
        self.city_manager = CityDataManager()

    def test_save_city(self):
        city = City(name="Test City", country_id="US")
        saved_city = self.city_manager.save(city)
        self.assertIsNotNone(saved_city.id)
        self.assertEqual(saved_city.name, "Test City")
        self.assertEqual(saved_city.country_id, "US")
        self.assertIsNotNone(saved_city.created_at)
        self.assertIsNotNone(saved_city.updated_at)

    def test_get_city(self):
        city = City(name="Test City", country_id="US")
        saved_city = self.city_manager.save(city)
        retrieved_city = self.city_manager.get(saved_city.id)
        self.assertIsNotNone(retrieved_city)
        self.assertEqual(retrieved_city.id, saved_city.id)

    def test_get_all_cities(self):
        city1 = City(name="City 1", country_id="US")
        city2 = City(name="City 2", country_id="US")
        self.city_manager.save(city1)
        self.city_manager.save(city2)
        cities = self.city_manager.get_all()
        self.assertEqual(len(cities), 2)

    def test_update_city(self):
        city = City(name="Test City", country_id="US")
        saved_city = self.city_manager.save(city)
        saved_city.name = "Updated City"
        updated_city = self.city_manager.update(saved_city)
        self.assertEqual(updated_city.name, "Updated City")

    def test_delete_city(self):
        city = City(name="Test City", country_id="US")
        saved_city = self.city_manager.save(city)
        self.assertTrue(self.city_manager.delete(saved_city.id))
        self.assertIsNone(self.city_manager.get(saved_city.id))

    def test_get_cities_by_country(self):
        city1 = City(name="City 1", country_id="US")
        city2 = City(name="City 2", country_id="US")
        city3 = City(name="City 3", country_id="UK")
        self.city_manager.save(city1)
        self.city_manager.save(city2)
        self.city_manager.save(city3)
        cities_us = self.city_manager.get_cities_by_country("US")
        cities_uk = self.city_manager.get_cities_by_country("UK")
        self.assertEqual(len(cities_us), 2)
        self.assertEqual(len(cities_uk), 1)

if __name__ == '__main__':
    unittest.main()
