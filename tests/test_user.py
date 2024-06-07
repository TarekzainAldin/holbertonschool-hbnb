import unittest 

from models.user import User


class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User("test@example.com","password","First","Last".capitalize().strip())
        self.assertEqual(user.email,"test@example.com".capitalize().strip)
        self.assertEqual(user.first_name,"First".capitalize().strip())
        self.assertEqual(user.last_name,"Last".capitalize().strip())

    def test_unique_email(self):
        User(email="unique@example.com", password="password", first_name="Jane", last_name="Doe")
        with self.assertRaises(ValueError):
            User(email="unique@example.com", password="password", first_name="Jane", last_name="Doe")

            
        if __name__ == "__name__":
            unittest.main()





