# tests/test_review.py

import unittest
from models.review import Review

class TestReviewModel(unittest.TestCase):
    def setUp(self):
        # Resetting the class attribute before each test
        Review._reviews = []

    def test_review_initialization(self):
        review = Review(review_id=1, user_id=101, place_id=202, rating=4.5, comment="Great place!")
        self.assertEqual(review.review_id, 1)
        self.assertEqual(review.user_id, 101)
        self.assertEqual(review.place_id, 202)
        self.assertEqual(review.rating, 4.5)
        self.assertEqual(review.comment, "Great place!")

    def test_calculate_average_rating_no_reviews(self):
        average_rating = Review.calculate_average_rating()
        self.assertEqual(average_rating, 0.0)

    def test_calculate_average_rating_with_reviews(self):
        Review(review_id=1, user_id=101, place_id=202, rating=4.5, comment="Great place!")
        Review(review_id=2, user_id=102, place_id=203, rating=3.5, comment="Good place.")
        average_rating = Review.calculate_average_rating()
        self.assertAlmostEqual(average_rating, 4.0, places=1)

    def test_multiple_reviews(self):
        Review(review_id=1, user_id=101, place_id=202, rating=4.5, comment="Great place!")
        Review(review_id=2, user_id=102, place_id=203, rating=3.5, comment="Good place.")
        Review(review_id=3, user_id=103, place_id=204, rating=5.0, comment="Excellent place!")
        self.assertEqual(len(Review._reviews), 3)
        average_rating = Review.calculate_average_rating()
        self.assertAlmostEqual(average_rating, 4.33, places=2)

if __name__ == '__main__':
    unittest.main()
