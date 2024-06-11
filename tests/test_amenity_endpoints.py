import unittest

class AmenityTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_amenity(self):
        response = self.app.post('/amenities/', json={'name': 'Pool'})
        self.assertEqual(response.status_code, 201)

    def test_get_amenity(self):
        amenity = Amenity(name='Wi-Fi')
        db.session.add(amenity)
        db.session.commit()

        response = self.app.get(f'/amenities/{amenity.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Wi-Fi')

    def test_update_amenity(self):
        amenity = Amenity(name='Gym')
        db.session.add(amenity)
        db.session.commit()

        response = self.app.put(f'/amenities/{amenity.id}', json={'name': 'Fitness Center'})
        self.assertEqual(response.status_code, 200)

        updated_amenity = Amenity.query.get(amenity.id)
        self.assertEqual(updated_amenity.name, 'Fitness Center')

    def test_delete_amenity(self):
        amenity = Amenity(name='Spa')
        db.session.add(amenity)
        db.session.commit()

        response = self.app.delete(f'/amenities/{amenity.id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
