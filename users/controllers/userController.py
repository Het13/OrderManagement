from flask import request, jsonify

from users.services import add, login, changeRole
from authorizaton import token_required, roles_required
from users.validations import validate


def admin_register():
	data = request.get_json()
	role = 'admin'
	if add.add(data, role):
		return jsonify(success={'message': 'Registered successfully'})
	return jsonify(error={'message': 'Error registering user'})


def login_user():
	token = login.login_user()
	if not token:
		return jsonify(failed={'message': 'login failed'})
	return jsonify(success={'token': token})


@token_required
@roles_required('admin')
def change_roles(user_id):
	new_role = request.json.get('new_role')
	if new_role not in ['user', 'admin']:
		return jsonify(error={'message': 'Invalid Role'})
	users = validate.get_user_ids()
	if user_id not in users:
		return jsonify(failed={'message': f'No user with id {user_id} found'})
	changeRole.change_roles(new_role, user_id)
	return jsonify(success={'message': f'Role of id:{user_id} updated to {new_role} successfully'})
