from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# enable cross-origin resource sharing
CORS(app)

from lessenger import routes
