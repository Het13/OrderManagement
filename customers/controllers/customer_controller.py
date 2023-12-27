from flask import jsonify
from customers.services import customer_services
from authorizaton import token_required, roles_required
from custom_errors import NotFoundError, DatabaseError
from validations import validate_request_body, check_duplicate_email


@validate_request_body(
	required_fields=['first_name', 'last_name', 'email', 'password', 'phone', 'address', 'username', 'gender'])
@check_duplicate_email()
def add_customer():
	try:
		customer_id = customer_services.add_customer()
		return jsonify(success={'message': 'Successfully added customer', 'customer_id': customer_id}), 200
	except DatabaseError:
		return jsonify(failed={'Failure': 'Failed to add customer'})


@token_required
@roles_required('admin')
def get_by_id(id):
	try:
		customer = customer_services.get_by_id(customer_id=id)
		return jsonify(success={'customer': customer}), 200
	except NotFoundError:
		return jsonify(failed={'message': f'No customer with id: {id} found'}), 200
	except DatabaseError:
		return jsonify(failed={'message': 'Failed to get customer'})


@token_required
@roles_required('admin')
def get_all():
	try:
		customers = customer_services.get_all()
		return jsonify(success={'customers': customers}), 200
	except NotFoundError:
		return jsonify(failed={'message': 'No data found'})
	except DatabaseError:
		return jsonify(failed={'message': 'Failed to get customers'})


@token_required
@roles_required('user', 'admin')
def get_orders(id):
	try:
		orders = customer_services.get_orders(customer_id=id)
		return jsonify(success={'orders': orders})
	except NotFoundError:
		return jsonify(failed={'message': f'No customer with id: {id} found'})
	except DatabaseError:
		return jsonify(failed={'message': 'Failed to get orders'})
