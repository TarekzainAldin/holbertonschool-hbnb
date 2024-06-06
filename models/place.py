#!/usr/bin/env python3
"""
This module contains classes representing model base.
"""
# models/place.py
from datetime import datetime

class Place:
    def __init__(self, id, name, description, price, user_id, city_id):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.user_id = user_id
        self.city_id = city_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.amenities = []
        self.reviews = []

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)
            self.updated_at = datetime.now()

    def get_reviews(self):
        return self.reviews

    def add_review(self, review):
        self.reviews.append(review)
        self.updated_at = datetime.now()
