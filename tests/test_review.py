import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_review_creation(self):
        review = Review(user_id="user1", place_id="place1", rating=5, comment="Great place!")
        self.assertIsInstance(review.id, str)
        self.assertEqual(review.user_id, "user1")
        self.assertEqual(review.place_id, "place1")
        self.assertEqual(review.rating, 5)

if __name__ == "__main__":
    unittest.main()
