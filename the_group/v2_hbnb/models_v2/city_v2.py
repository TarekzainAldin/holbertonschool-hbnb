from datetime import datetime

class City:
    def __init__(self, name, country_code):
        self.id = None
        self.name = name
        self.country_code = country_code
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'country_code': self.country_code,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
