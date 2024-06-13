from datetime import datetime
from.base_model import BaseModel


class Review(BaseModel):
    def __init__(self, review_id, user_id, place_id, rating, comment):
        self.review_id = review_id
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment
        # Adding the instance to the class attribute list
        Review._reviews.append(self)

    @classmethod
    def calculate_average_rating(cls) -> float:
        """
        Calculates and returns the average rating of all reviews.
        """
        if not cls._reviews:
            return 0.0
        total_rating = sum(review.rating for review in cls._reviews)
        return total_rating / len(cls._reviews)
