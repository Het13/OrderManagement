from flask import request


def is_empty_new_attributes():
	customer_id = request.form.get('customer_id')
	payment_mode = request.form.get('payment_mode')

	product_id = request.form.get('product_id')
	product_quantity = request.form.get('product_quantity')

	if customer_id is None or customer_id == '' \
			or payment_mode is None or payment_mode == '' \
			or product_id is None or product_id == '' \
			or product_quantity is None or product_quantity == '':
		return True
	return False


def is_empty_modify_attributes():
	product_id = request.form.get('product_id')
	product_quantity = request.form.get('product_quantity')

	if product_id is None or product_id == '' \
			or product_quantity is None or product_quantity == '':
		return True
	return False
