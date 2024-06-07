from datetime import datetime
from.base_model import BaseModel


class Review(BaseModel):
    def __init__(self, review_id, user_id, place_id, rating, comment):
        self.review_id = review_id
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
