from datetime import datetime

class User:
    def __init__(self, email, first_name, last_name):
        self.id= None
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.places = []  # List to hold the places owned by the user
        self.reviews = []  # List to hold the reviews written by the user
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def add_place(self, place):
        self.places.append(place)

    def add_review(self, review):
        self.reviews.append(review)

    def __repr__(self):
        return f"User(email='{self.email}', first_name='{self.first_name}', last_name='{self.last_name}')"
