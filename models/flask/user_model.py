#!/usr/bin/python3
from datetime import datetime
users = {}

class User:
    def __init__(self, email, first_name, last_name):
        self.id = str(uuid.uuid4())
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
