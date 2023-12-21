from flask import request
from databaseConnection import database_connection


def is_empty_header_attributes(customer_id, order_status, payment_mode, shipper_id):
	if customer_id is None or customer_id == '' \
			or order_status is None or order_status == '' \
			or payment_mode is None or payment_mode == '' \
			or shipper_id is None or shipper_id == '':
		return True
	return False


def is_empty_items_attributes(product_id, product_quantity):
	if product_id is None or product_id == '' \
			or product_quantity is None or product_quantity == '':
		return True
	return False


def get_header_attributes():
	customer_id = request.form.get('customer_id')
	order_date = request.form.get('date')
	order_status = request.form.get('status')
	payment_mode = request.form.get('payment_mode')
	payment_date = request.form.get('payment_date')
	order_shipment_date = request.form.get('shipment_date')
	shipper_id = request.form.get('shipment_id')

	if is_empty_header_attributes(customer_id, order_status, payment_mode, shipper_id):
		return False

	new_order_header_data = (
		customer_id,
		order_date,
		order_status,
		payment_mode,
		payment_date,
		order_shipment_date,
		shipper_id
	)

	return new_order_header_data


def get_items_attributes(order_id):
	product_id = request.form.get('product_id')
	product_quantity = request.form.get('product_quantity')

	if is_empty_items_attributes(product_id, product_quantity):
		return False

	new_order_items_data = [(
		order_id,
		curr_product_id,
		curr_product_quantity
	) for (curr_product_id, curr_product_quantity) in zip(product_id.split(), product_quantity.split())]

	return new_order_items_data


def add_order():
	database, database_cursor = database_connection()

	new_order_header_insert_stmt = "INSERT INTO ORDER_HEADER (CUSTOMER_ID, ORDER_DATE, ORDER_STATUS, " \
	                               "PAYMENT_MODE, PAYMENT_DATE, ORDER_SHIPMENT_DATE, SHIPPER_ID) " \
	                               "VALUES(%s,%s,%s,%s,%s,%s,%s)"

	new_order_items_insert_stmt = "INSERT INTO ORDER_ITEMS (ORDER_ID, PRODUCT_ID, PRODUCT_QUANTITY) VALUES (%s,%s,%s)"

	header_attributes = get_header_attributes()
	if not header_attributes:
		return False

	new_order_header_data = header_attributes

	database_cursor.execute(new_order_header_insert_stmt, new_order_header_data)
	order_id = database_cursor.lastrowid

	items_attributes = get_items_attributes(order_id)
	if not items_attributes:
		return False
	new_order_items_data = items_attributes
	database_cursor.executemany(new_order_items_insert_stmt, new_order_items_data)

	database.commit()
	database.close()

	return order_id
