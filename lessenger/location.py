from flask_googlemaps import GoogleMaps
import requests

from lessenger import app

GOOGLE_API_KEY = "AIzaSyD7W7v5psM8TDJwUV2WxsPkoYRtByh07Y0"

GoogleMaps(app, key=GOOGLE_API_KEY)

base_url = "https://maps.googleapis.com/maps/api/geocode/json"


def _get_location_details(location):
    """Returns the location search string using Google's geolocation API
    (https://developers.google.com/maps/documentation/geocoding/start).
    
    Return:
        JSON object of geolocation results data, as described by docs

    """
    resp = requests.get(
        base_url,
        params = {
            'address': ''.join(location.split(' ')),
            'key': GOOGLE_API_KEY,
        }
    )
    return resp.json()

def get_lat_long(location):
    """Returns the latitude and longitude of a location search string.

    Args:
        location (str): text of a location

    Returns:
        tuple: ((u'lat', 37.4224082), (u'lng', -122.0856086))

    Example: 
        get_lat_long("1600 Amphitheatre Parkway, Mountain View, CA")
        >>> ((u'lat', 37.4224082), (u'lng', -122.0856086))

    """
    location_details = _get_location_details(location)
    lat, lon = location_details['results'][0]['geometry']['location'].items()
    return lat, lon
