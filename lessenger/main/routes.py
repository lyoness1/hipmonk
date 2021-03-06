from flask import Blueprint, request, jsonify, render_template

from lessenger.location.model import Geolocator

main = Blueprint('main', __name__)


@main.route('/')
def index():
	locator = Geolocator()
	lat, lon = locator.get_lat_long("1600 Amphitheatre Parkway, Mountain View, CA")
	return jsonify(lat[1], lon[1])

@main.route('/chat/messages', methods = ['POST'])
def lessenger():
	data = request.form
	resp = {"messages": []}

	if request.method == 'POST':
		if data['action'] == 'join': 
			resp['messages'].append({
				"type": "text", 
				"text": "Welcome, {name}".format(name=request.form['name']),
			})

		elif data['action'] == 'message':
			pass

	return jsonify(resp)
