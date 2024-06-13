#!/usr/bin/python3
"""Data manager for the application."""


from persistence.place_repository import PlaceRepository


class DataManager:
    """Class to manage CRUD operations for various entities."""
    def __init__(self):
        self.place_repository = PlaceRepository()


    # Methods for Place
    def save_place(self, place_data):
        place = place(**place_data)
        self.place_repository.save(place)
        return place.place_id

    def get_place(self, place_id):
        return self.place_repository.get(place_id)

    def update_place(self, place_id, new_data):
        return self.place_repository.update(place_id, new_data)

    def delete_place(self, place_id):
        return self.place_repository.delete(place_id)

    def get_all_places(self):
        return self.place_repository.get_all()


