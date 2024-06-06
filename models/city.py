#!/usr/bin/python3
"""Define city class"""

from base_model import BaseModel
import uuid
from datetime import datetime


class City(BaseModel):
    """Represents a city"""
    def __init__(self, name, country):
        """initialize a new city"""
        super().__init__()
        self.id = uuid.uuid4()
        self.name = name
        self.country_id = country.id
        self.country = country
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.places = []

    def add_place(self, place):
         """Add a place to the city"""
         if place not in self.places:
             self.places.append(place)
             self.updated_at = datetime.now()

    def get_place(self):
        """Get all places in the city"""
        return self.places
