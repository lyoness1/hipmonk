from flask import request, jsonify
from lessenger import app

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/chat/messages', methods = ['POST'])
def lessenger():
	if request.method == 'POST':
		resp = {"messages": []}
		data = request.form
		if data['action'] == 'join': 
			resp['messages'].append({
				"type": "text", 
				"text": "Welcome, {name}".format(name=request.form['name']),
			})

		elif data['action'] == 'message':
			pass

		return jsonify(resp)
