# tests/test_user.py
import unittest
from datetime import datetime
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User("test@example.com", "John", "Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

    def test_add_place(self):
        user = User("test@example.com", "John", "Doe")
        user.add_place("New Place")
        self.assertEqual(len(user.places), 1)
        self.assertEqual(user.places[0], "New Place")

    # Add more tests for other methods and business logic

if __name__ == '__main__':
    unittest.main()