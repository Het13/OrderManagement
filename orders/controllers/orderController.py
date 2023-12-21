from flask import jsonify
from orders.services import new, modify
from orders.validations import validate


def add_order():
	if validate.is_empty_new_attributes():
		return jsonify(error={'message': 'Empty Fields'}), 400
	return jsonify(success={'message': 'Successfully added new order.', 'order_id': new.add_order()}), 200


def modify_order(order_id):
	if validate.is_empty_modify_attributes():
		return jsonify(error={'message': 'Empty Fields'}), 400
	result= modify.modify_order(order_id)
	if result:
		return jsonify(success={'message': 'Successfully modified order'}), 200
	return jsonify(failed={'message': f'No order with id:{order_id} found'}), 200
