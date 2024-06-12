from datetime import datetime
import uuid
import json

class Place:
    def __init__(self, name, description, address, city_id, latitude, longitude, host_id,
                 number_of_rooms, number_of_bathrooms, price_per_night, max_guests):
        self.id = uuid.uuid4()
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
        self.updated_at = datetime.now()

    def add_review(self, review):
        self.reviews.append(review)
        self.updated_at = datetime.now()

    def __repr__(self):
        return f"Place(name='{self.name}', city_id='{self.city_id}', host_id='{self.host_id}')"

    def set_host(self, host):
        if not isinstance(host, User):
            raise ValueError("Host must be a User object")
        self.host_id = host.email

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "city_id": str(self.city_id),
            "latitude": self.latitude,
            "longitude": self.longitude,
            "host_id": str(self.host_id),
            "number_of_rooms": self.number_of_rooms,
            "number_of_bathrooms": self.number_of_bathrooms,
            "price_per_night": self.price_per_night,
            "max_guests": self.max_guests,
            "amenities": [str(amenity.id) for amenity in self.amenities],  # Assuming Amenity objects have 'id' attributes
            "reviews": [str(review.id) for review in self.reviews],  # Assuming Review objects have 'id' attributes
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def from_json(cls, json_data):
        place_data = json.loads(json_data)
        place = cls(
            place_data["name"],
            place_data["description"],
            place_data["address"],
            uuid.UUID(place_data["city_id"]),
            place_data["latitude"],
            place_data["longitude"],
            uuid.UUID(place_data["host_id"]),
            place_data["number_of_rooms"],
            place_data["number_of_bathrooms"],
            place_data["price_per_night"],
            place_data["max_guests"]
        )
        place.id = uuid.UUID(place_data["id"])
        place.created_at = datetime.fromisoformat(place_data["created_at"])
        place.updated_at = datetime.fromisoformat(place_data["updated_at"])
        # Assuming we have a way to convert amenity and review IDs back to objects
        place.amenities = [Amenity.get_by_id(amenity_id) for amenity_id in place_data["amenities"]]
        place.reviews = [Review.get_by_id(review_id) for review_id in place_data["reviews"]]
        return place

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.to_json(), file)

    @classmethod
    def load_from_json(cls, filename):
        with open(filename, 'r') as file:
            json_data = json.load(file)
            return cls.from_json(json.dumps(json_data))
