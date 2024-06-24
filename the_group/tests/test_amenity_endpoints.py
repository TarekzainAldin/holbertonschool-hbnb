import unittest
from unittest.mock import patch, MagicMock
from myapp import app, db, Amenity

class AmenityTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    @patch('myapp.db.session.add')
    @patch('myapp.db.session.commit')
    def test_create_amenity(self, mock_commit, mock_add):
        response = self.app.post('/amenities/', json={'name': 'Pool'})
        self.assertEqual(response.status_code, 201)
        mock_add.assert_called_once()
        mock_commit.assert_called_once()

    @patch('myapp.Amenity.query.get')
    def test_get_amenity(self, mock_get):
        mock_amenity = MagicMock()
        mock_amenity.id = 1
        mock_amenity.name = 'Wi-Fi'
        mock_get.return_value = mock_amenity

        response = self.app.get(f'/amenities/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Wi-Fi')

    @patch('myapp.db.session.commit')
    @patch('myapp.Amenity.query.get')
    def test_update_amenity(self, mock_get, mock_commit):
        mock_amenity = MagicMock()
        mock_amenity.id = 1
        mock_amenity.name = 'Gym'
        mock_get.return_value = mock_amenity

        response = self.app.put(f'/amenities/1', json={'name': 'Fitness Center'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_amenity.name, 'Fitness Center')
        mock_commit.assert_called_once()

    @patch('myapp.db.session.commit')
    @patch('myapp.db.session.delete')
    @patch('myapp.Amenity.query.get')
    def test_delete_amenity(self, mock_get, mock_delete, mock_commit):
        mock_amenity = MagicMock()
        mock_amenity.id = 1
        mock_amenity.name = 'Spa'
        mock_get.return_value = mock_amenity

        response = self.app.delete(f'/amenities/1')
        self.assertEqual(response.status_code, 204)
        mock_delete.assert_called_once_with(mock_amenity)
        mock_commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
