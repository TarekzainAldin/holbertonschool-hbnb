from persistence.IPersistenceManager import IPersistenceManager
from models.place import Place

class PlaceDataManager(IPersistenceManager):
    def __init__(self):
        self.places = {}
        self.next_id = 1

    def save(self, place):
        """Saves a place."""
        if not isinstance(place, Place):
            raise ValueError("Can only save instances of Place")

        if place.place_id is None:
            place.place_id = self.next_id
            self.next_id += 1
        self.places[place.place_id] = place

    def get(self, place_id):
        """Fetches a place."""
        return self.places.get(place_id)

    def get_all(self):
        """Fetches all places."""
        return list(self.places.values())

    def update(self, place_id, new_place_data):
        """Updates an existing place."""
        if place_id in self.places:
            place = self.places[place_id]
            place.update_place_data(new_place_data)
            self.save(place)
            return True
        return False

    def delete(self, place_id):
        """Deletes an existing place."""
        if place_id in self.places:
            del self.places[place_id]
            return True
        return False
