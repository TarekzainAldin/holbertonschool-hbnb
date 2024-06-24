# persistence/review_repository.py

from models.review import Review

class ReviewRepository:
    def __init__(self):
        self.reviews = {}
        self.next_id = 1

    def save(self, review_data):
        """Saves a review."""
        review_id = str(self.next_id)
        review = Review(
            review_id=review_id,
            user_id=review_data['user_id'],
            place_id=review_data['place_id'],
            rating=review_data['rating'],
            comment=review_data.get('comment', ''),
        )
        self.reviews[review_id] = review
        self.next_id += 1

    def get(self, review_id):
        """Fetches a review."""
        return self.reviews.get(review_id)

    def get_all(self):
        """Fetches all reviews."""
        return list(self.reviews.values())

    def update(self, review_id, new_review_data):
        """Updates an existing review."""
        if review_id in self.reviews:
            review = self.reviews[review_id]
            for key, value in new_review_data.items():
                if hasattr(review, key):
                    setattr(review, key, value)
                else:
                    raise AttributeError(f"Invalid field: {key}")
            return True
        return False

    def delete(self, review_id):
        """Deletes an existing review."""
        if review_id in self.reviews:
            del self.reviews[review_id]
            return True
        return False
