from flask import request, jsonify

from users.services.add import add
from users.services.login import login_user



def admin_register():
	data = request.get_json()
	role = 'admin'
	if add(data, role):
		return jsonify(success={'message': 'Registered successfully'})
	return jsonify(error={'message': 'Error registering user'})


def login():
	token = login_user()
	if not token:
		return jsonify(failed={'message': 'login failed'})
	return jsonify(success={'token': token})
