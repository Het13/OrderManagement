from flask import jsonify
from customers.services import new, getByID, getAll, getOrders
from customers.validations import validate
from authorizaton import token_required, roles_required


def add_customer():
	if validate.check_empty_attributes():
		return jsonify(error={'Failed': 'Empty Fields'}), 400
	if not validate.is_unique_email():
		return jsonify(error={'message': 'Duplicate email'}), 409
	result = new.add_customer()

	return jsonify(success={'message': 'Successfully added customer', 'customer_id': result}), 200


@token_required
@roles_required('admin')
def get_by_id(id):
	result = getByID.get_by_id(id)
	if not result:
		return jsonify(failed={'message': f'No customer with id: {id} found'}), 200
	return jsonify(customer=result), 200


@token_required
@roles_required('admin')
def get_all():
	return jsonify(all_customers=getAll.get_all()), 200


@token_required
@roles_required('user', 'admin')
def get_orders(id):
	result, data = getOrders.get_orders(id)
	if result:
		return jsonify(success={'orders': data})
	return jsonify(failed={'message': data})
