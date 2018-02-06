import requests

from routes import GOOGLE_API_KEY

class Geolocator():
    def __init__(self):
        self.base_url = "https://maps.googleapis.com/maps/api/geocode/json"

    def _get_location_details(self, location):
        """Returns the location search string using Google's geolocation API
        (https://developers.google.com/maps/documentation/geocoding/start).
        
        Return:
            JSON object of geolocation results data, as described by docs

        """
        resp = requests.get(
            self.base_url,
            params = {
                'address': ''.join(location.split(' ')),
                'key': GOOGLE_API_KEY,
            }
        )
        return resp.json()

    def get_lat_long(self, location):
        """Returns the latitude and longitude of a location search string.

        Args:
            location (str): text of a location

        Returns:
            tuple: ((u'lat', 37.4224082), (u'lng', -122.0856086))

        Example: 
            get_lat_long("1600 Amphitheatre Parkway, Mountain View, CA")
            >>> ((u'lat', 37.4224082), (u'lng', -122.0856086))

        """
        location_details = self._get_location_details(location)
        lat, lon = location_details['results'][0]['geometry']['location'].items()
        return lat, lon
