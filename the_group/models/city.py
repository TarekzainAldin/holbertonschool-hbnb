import json
from .base_model import BaseModel
from datetime import datetime
import uuid


class City(BaseModel):
    """Represents a city"""

    def __init__(self, name, country):
        """Initialize a new city"""
        super().__init__()
        self.name = name
        self.country_id = country.id
        self.country = country
        self.places = []

    def add_place(self, place):
        """Add a place to the city"""
        if place not in self.places:
            self.places.append(place)
            self.updated_at = datetime.now()

    def get_places(self):
        """Get all places in the city"""
        return self.places

    def to_dict(self):
        """Return a dictionary representation of the city"""
        city_dict = super().to_dict()
        city_dict.update({
            'name': self.name,
            'country_id': self.country_id,
            'places': [place.id for place in self.places]
        })
        return city_dict

    @classmethod
    def from_dict(cls, dict_data, country):
        """Create a City object from a dictionary"""
        city = cls(dict_data['name'], country)
        city.id = dict_data['id']
        city.created_at = datetime.fromisoformat(dict_data['created_at'])
        city.updated_at = datetime.fromisoformat(dict_data['updated_at'])
        city.places = dict_data['places']  # This should be updated to include actual place objects later
        return city

    def to_json(self):
        """Return a JSON string representation of the city"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_data, country):
        """Create a City object from a JSON string"""
        dict_data = json.loads(json_data)
        return cls.from_dict(dict_data, country)

    def save_to_json(self, filename):
        """Save the city object to a JSON file"""
        with open(filename, 'w') as file:
            json.dump(self.to_dict(), file)
