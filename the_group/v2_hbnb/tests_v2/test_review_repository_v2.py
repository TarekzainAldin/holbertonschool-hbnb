# tests/test_review_repository.py

import unittest
from datetime import datetime
import sys
import os

# Add the root directory of the project to the import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from models.review import Review
from persistence.review_repository import ReviewRepository

class TestReviewRepository(unittest.TestCase):
    def setUp(self):
        self.repo = ReviewRepository()
        self.review1_data = {
            'user_id': 1,
            'place_id': 1,
            'rating': 5,
            'comment': 'Great product',
        }
        self.review2_data = {
            'user_id': 2,
            'place_id': 2,
            'rating': 4,
            'comment': 'Not satisfied',
        }

    def test_save(self):
        self.repo.save(self.review1_data)
        self.assertEqual(len(self.repo.reviews), 1)

        saved_review = list(self.repo.reviews.values())[0]
        self.assertEqual(saved_review.user_id, 1)
        self.assertEqual(saved_review.place_id, 1)
        self.assertEqual(saved_review.rating, 5)
        self.assertEqual(saved_review.comment, 'Great product')

    def test_get(self):
        self.repo.save(self.review1_data)
        self.repo.save(self.review2_data)

        retrieved_review1 = self.repo.get('1')
        self.assertEqual(retrieved_review1.user_id, 1)
        self.assertEqual(retrieved_review1.place_id, 1)
        self.assertEqual(retrieved_review1.rating, 5)
        self.assertEqual(retrieved_review1.comment, 'Great product')

        retrieved_review2 = self.repo.get('2')
        self.assertEqual(retrieved_review2.user_id, 2)
        self.assertEqual(retrieved_review2.place_id, 2)
        self.assertEqual(retrieved_review2.rating, 4)
        self.assertEqual(retrieved_review2.comment, 'Not satisfied')

        self.assertIsNone(self.repo.get('3'))  # Test for non-existent review

    def test_update(self):
        self.repo.save(self.review1_data)
        updated_data = {'rating': 4, 'comment': 'Updated comment'}
        self.assertTrue(self.repo.update('1', updated_data))

        updated_review = self.repo.get('1')
        self.assertEqual(updated_review.rating, 4)
        self.assertEqual(updated_review.comment, 'Updated comment')

        # Test update with non-existent review_id
        self.assertFalse(self.repo.update('100', updated_data))

    def test_delete(self):
        self.repo.save(self.review1_data)
        self.repo.save(self.review2_data)

        self.assertTrue(self.repo.delete('1'))
        self.assertEqual(len(self.repo.reviews), 1)
        self.assertIsNone(self.repo.get('1'))

        # Test delete with non-existent review_id
        self.assertFalse(self.repo.delete('100'))

    def test_save_invalid_review(self):
        with self.assertRaises(KeyError):
            self.repo.save({})  # Missing required fields

    def test_update_invalid_review(self):
        self.repo.save(self.review1_data)
        with self.assertRaises(AttributeError):
            self.repo.update('1', {'invalid_field': 'value'})

    def test_get_non_existent_review(self):
        self.assertIsNone(self.repo.get('100'))

if __name__ == '__main__':
    unittest.main()
