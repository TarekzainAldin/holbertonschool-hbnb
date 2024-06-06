#!/usr/bin/python3
"""Define user class"""
from base_model import BaseModel


class User(BaseModel):
    def __init__(self, email, password, first_name, last_name):
        """Initialize a new User instance"""
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        """Return the dictionary of the User instance, including inherited attributes"""
        user_dict = super().to_dict()
        user_dict.update({
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name
        })
        return user_dict