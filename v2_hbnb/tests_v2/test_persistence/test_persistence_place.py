#!/usr/bin/python3
import unittest
from unittest.mock import MagicMock
import sys
import os

# Ajouter le répertoire racine du projet au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from models.place import Place
from persistence.place_repository import PlaceRepository

class TestPlaceRepository(unittest.TestCase):

    def setUp(self):
        self.repo = PlaceRepository()
        self.place = Place(name="Sample Place", description="A nice place", address="123 Main St",
                           city_id=1, latitude=0.0, longitude=0.0, host_id=1, number_of_rooms=2,
                           number_of_bathrooms=1, price_per_night=100, max_guests=4, amenity_ids=[])

    def test_save(self):
        # Test saving a new place
        self.repo.save(self.place)
        self.assertIn(self.place.place_id, self.repo.places)
        self.assertEqual(self.repo.places[self.place.place_id], self.place)

        # Test saving an object that is not an instance of Place
        with self.assertRaises(ValueError):
            self.repo.save("not_a_place")

    def test_get(self):
        # Test getting a place
        self.repo.save(self.place)
        fetched_place = self.repo.get(self.place.place_id)
        self.assertEqual(fetched_place, self.place)

        # Test getting a non-existent place
        self.assertIsNone(self.repo.get("non_existent_id"))

    def test_get_all(self):
        # Test getting all places
        self.repo.save(self.place)
        all_places = self.repo.get_all()
        self.assertEqual(len(all_places), 1)
        self.assertEqual(all_places[0], self.place)

    def test_update(self):
        # Mock the update_place_data method in the Place class
        self.place.update_place_data = MagicMock()

        # Test updating an existing place
        self.repo.save(self.place)
        new_data = {"name": "Updated Place"}
        result = self.repo.update(self.place.place_id, new_data)
        self.place.update_place_data.assert_called_once_with(new_data)
        self.assertTrue(result)

        # Test updating a non-existent place
        result = self.repo.update("non_existent_id", new_data)
        self.assertFalse(result)

    def test_delete(self):
        # Test deleting an existing place
        self.repo.save(self.place)
        result = self.repo.delete(self.place.place_id)
        self.assertNotIn(self.place.place_id, self.repo.places)
        self.assertTrue(result)

        # Test deleting a non-existent place
        result = self.repo.delete("non_existent_id")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
