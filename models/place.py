#!/usr/bin/env python3
"""
This module contains classes representing model base.
"""
from datetime import datetime
from models.base_model import BaseModel


class Place(BaseModel):
    def __init__(self, name, description, address, city_id, latitude,
                 longitude, host_id, num_rooms, num_bathrooms, price_per_night,
                 max_guests, amenities):
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = amenities

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.add(amenity)
            self.updated_at = datetime.now()

    def get_reviews(self):
        return self.reviews

    def add_review(self, review):
        self.reviews.append(review)
        self.updated_at = datetime.now()
