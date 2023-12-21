from flask import jsonify
from orders.services import new, modify


def add_order():
	result = new.add_order()
	if result:
		return jsonify(success={'message': 'Successfully added new order.', 'order_id': result}), 200
	return jsonify(error={'message': 'Empty Fields'}), 400


def modify_order(order_id):
	result, message = modify.modify_order(order_id)
	if result:
		return jsonify(success={'message': message}), 200
	return jsonify(failed={'message': message}), 400
