#!/usr/bin/env python3
"""
This module contains classes representing model base.
"""
import uuid
# models/place.py
from datetime import datetime

class Place:
    def __init__(self, name, description, price, user, city):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.price = price
        self.user_id = user
        self.city_id = city.id
        self.city = city
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

    def save(self):
        """Update updated_at and simulate saving to a database"""
        self.updated_at = datetime.now()
        pass
