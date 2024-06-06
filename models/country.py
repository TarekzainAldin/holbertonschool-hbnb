#!/usr/bin/python3
"""Define Coutnry class"""
from base_model import BaseModel


class Country(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.cities = []

    def add_city(self, city):
        self.cities.append(city)
        city.country = self

    def to_dict(self):
        dict_representation = super().to_dict()
        dict_representation['cities'] = [city.to_dict() for city in self.cities]
        return dict_representation