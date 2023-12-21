from flask import request
from databaseConnection import database_connection


def get_header_attributes():
	customer_id = request.form.get('customer_id')
	order_date = request.form.get('date')
	order_status = request.form.get('status')
	payment_mode = request.form.get('payment_mode')
	payment_date = request.form.get('payment_date')
	order_shipment_date = request.form.get('shipment_date')
	shipper_id = request.form.get('shipment_id')

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

	new_order_header_data = get_header_attributes()
	database_cursor.execute(new_order_header_insert_stmt, new_order_header_data)
	order_id = database_cursor.lastrowid

	new_order_items_data = get_items_attributes(order_id)
	database_cursor.executemany(new_order_items_insert_stmt, new_order_items_data)

	database.commit()
	database.close()

	return order_id
