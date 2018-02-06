from flask import Blueprint

GOOGLE_API_KEY = "AIzaSyD7W7v5psM8TDJwUV2WxsPkoYRtByh07Y0"

location = Blueprint('location', __name__)

@location.route('/')
def index():
    pass
