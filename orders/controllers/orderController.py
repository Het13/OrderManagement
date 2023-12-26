from flask import jsonify
from orders.services import new, modify, updateStatus, updateShipperID, cancel
from orders.validations import validate
from authorizaton import token_required, roles_required


@token_required
@roles_required('user')
def add_order():
	if validate.is_empty_new_attributes():
		return jsonify(error={'message': 'Empty Fields'}), 400
	return jsonify(success={'message': 'Successfully added new order.', 'order_id': new.add_order()}), 200


@token_required
@roles_required('user')
def modify_order(order_id):
	if validate.is_empty_modify_attributes():
		return jsonify(error={'message': 'Empty Fields'}), 400
	result = modify.modify_order(order_id)
	if result:
		return jsonify(success={'message': 'Successfully modified order'}), 200
	return jsonify(failed={'message': f'No order with id: {order_id} found'}), 200


@token_required
@roles_required('admin')
def update_status(order_id):
	result = updateStatus.update_status(order_id)
	if result:
		return jsonify(success={'message': 'successfully modified order status'}), 200
	return jsonify(failed={'message': f'No order with id: {order_id} found'}), 404


@token_required
@roles_required('admin')
def update_shipper_id(order_id):
	result = updateShipperID.update_shipper_id(order_id)
	if result:
		return jsonify(success={'message': 'Successfully modified shipper_id'}), 200
	return jsonify(failed={'message': f'No order with id: {order_id} found'}), 404


@token_required
@roles_required('admin', 'user')
def cancel_order(order_id):
	if cancel.cancel_order(order_id):
		return jsonify(success={'message': f'Order with id: {order_id} cancelled'}), 200
	return jsonify(failed={'message': f'No order with id: {order_id} found'})
