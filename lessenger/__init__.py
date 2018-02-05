from flask import Flask
from flask_googlemaps import GoogleMaps
from flask_cors import CORS

from lessenger.main.routes import main
from lessenger.location.routes import location

# create app
app = Flask(__name__)

# register Flask blueprints
app.register_blueprint(main)
app.register_blueprint(location, url_prefix='/location')

# enable cross-origin resource sharing
CORS(app)

# set up Google Maps
from location.routes import GOOGLE_API_KEY
GoogleMaps(app, key=GOOGLE_API_KEY)
