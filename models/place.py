from datetime import datetime

from models.user import User

class Place:
    def __init__(self, name, description, address, city_id, latitude, longitude, host_id, 
                 number_of_rooms, number_of_bathrooms, price_per_night, max_guests):
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = []  # List to hold Amenity objects
        self.reviews = []  # List to hold Review objects
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

    def add_review(self, review):
        self.reviews.append(review)

    def __repr__(self):
        return f"Place(name='{self.name}', city_id='{self.city_id}', host_id='{self.host_id}')"

    def set_host(self, host):
        if not isinstance(host, User):
            raise ValueError("Host must be a User object")
        self.host_id = host.email
