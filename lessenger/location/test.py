import unittest

from model import Geolocator

class TestGeolocator(unittest.TestCase):

    def setUp(self):
        self.locator = Geolocator()

    def test_get_lat_long_from_address(self):
        address = "1600 Amphitheatre Parkway, Mountain View, CA"
        lat, lon = self.locator.get_lat_long(address)
        self.assertEqual(lat[1], 37.4224082)
        self.assertEqual(lon[1], -122.0856086)

    def test_get_lat_long_from_city(self):
        address = "San Francisco"
        lat, lon = self.locator.get_lat_long(address)
        self.assertEqual(type(lat[1]), float)
        self.assertEqual(type(lon[1]), float)

    def test_get_lat_long_from_city_code(self):
        address = "SF"
        lat, lon = self.locator.get_lat_long(address)
        self.assertEqual(type(lat[1]), float)
        self.assertEqual(type(lon[1]), float)

    def test_get_lat_long_from_zip(self):
        address = "94131"
        lat, lon = self.locator.get_lat_long(address)
        self.assertEqual(type(lat[1]), float)
        self.assertEqual(type(lon[1]), float)


if __name__ == '__main__':
    unittest.main()
