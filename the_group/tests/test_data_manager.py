# Save this code in test_data_manager.py
import unittest
from persistence.data_manager  import DataManager

class TestDataPersistence(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()

    def test_save_and_retrieve_entity(self):
        # Your test cases here
        pass

if __name__ == '__main__':
    unittest.main()
