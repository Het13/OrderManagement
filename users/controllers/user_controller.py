from flask import request, jsonify

from users.services import user_services
from middleware.authorizaton import token_required, roles_required
from middleware.custom_errors import NotFoundError, DatabaseError, LoginError
from middleware.validations import validate_request_body


@validate_request_body(required_fields=['email', 'password'])
def admin_register():
	data = request.get_json()
	role = 'admin'
	try:
		user_services.add(data, role)
		return jsonify(success={'message': 'Registered successfully'})
	except DatabaseError:
		return jsonify(error={'message': 'Error registering user'})


def login_user():
	try:
		token = user_services.login_user()
		return jsonify(success={'message': 'Login successful', 'token': token})
	except LoginError:
		return jsonify(failed={'message': 'Invalid credentials'})
	except NotFoundError:
		return jsonify(failed={'message': 'User not found'})
	except DatabaseError:
		return jsonify(failed={'message': 'Login failed'})


@token_required
@roles_required('admin')
@validate_request_body(required_fields=['new_role'])
def change_roles(user_id):
	new_role = request.json.get('new_role')
	if new_role not in ['user', 'admin']:
		return jsonify(error={'message': 'Invalid Role'})

	try:
		user_services.change_roles(new_role, user_id)
		return jsonify(success={'message': f'Role updated to {new_role} successfully'})
	except NotFoundError:
		return jsonify(failed={'message': 'User not found'})
	except DatabaseError:
		return jsonify(failed={'message': 'Failed to update role'})
