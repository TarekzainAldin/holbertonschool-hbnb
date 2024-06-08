# model/amenity.py
class Amenity:
    def __init__(self, name):
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self):
        return f"Amenity(name='{self.name}')"