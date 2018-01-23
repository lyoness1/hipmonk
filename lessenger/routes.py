from flask import request, jsonify, render_template

from lessenger import app
from location import get_lat_long


@app.route('/')
def index():
	lat, lon = get_lat_long("1600 Amphitheatre Parkway, Mountain View, CA")
	return jsonify(lat[1], lon[1])

@app.route('/chat/messages', methods = ['POST'])
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
