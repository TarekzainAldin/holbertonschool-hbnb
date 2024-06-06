import unittest
from models.place import Place 
class TestPlace( unittest.TestCase):
  def Test_place_creation(self):
    place = place("Test Place", "A test description","123 Test st","1",10.0,10.0,"1",3,2,100,4,["WiFi"])
    self.assertEqual(place.name,"nice place")
    self.assertAlmostEqual(place.adderss,"123 address st")

    if __name__ == "__main__":
     unittest.main()
     