#!/usr/bin/python3
"""Define city class"""

from base_model import BaseModel
import uuid
from datetime import datetime


class City(BaseModel):
    """Represents a city"""
    def __init__(self, name, country_id):
        """initialize a new country"""
        super().__init__()
        self.id = uuid.uuid4()
        self.name = name
        self.country_id = country_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def operation1(self, params):
        """Sample operation1 method"""
        return type(params)

    def operation2(self, params):
        """Sample operation2 method"""
        pass

    def save (self):
        """Update updated_at and simulate saving to a database"""
        self.updated_at = datetime.now()
        pass


