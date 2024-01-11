from flask import request
from database_connection import connection_pool
from middleware.custom_errors import NotFoundError, DatabaseError


def get_header_attributes(customer_id):
	request_body = request.get_json()
	order_date = None
	order_status = None
	payment_mode = request_body['payment_mode']
	payment_date = None
	order_shipment_date = None
	shipper_id = None

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


def add_order(customer_id):
	connection = connection_pool.get_connection()
	database_cursor = connection.cursor()

	try:
		new_order_header_insert_stmt = "INSERT INTO ORDER_HEADER (CUSTOMER_ID, ORDER_DATE, ORDER_STATUS, " \
		                               "PAYMENT_MODE, PAYMENT_DATE, ORDER_SHIPMENT_DATE, SHIPPER_ID) " \
		                               "VALUES(%s,%s,%s,%s,%s,%s,%s)"

		new_order_header_data = get_header_attributes(customer_id)
		database_cursor.execute(new_order_header_insert_stmt, new_order_header_data)
		order_id = database_cursor.lastrowid
		connection.commit()
		return order_id
	except:
		raise DatabaseError
	finally:
		database_cursor.close()
		connection.close()


def get_items_attributes(order_id):
	request_body = request.get_json()
	products = request_body['products']

	product_id = []
	product_quantity = []
	for product in products:
		product_id.append(product['id'])
		product_quantity.append(product['quantity'])

	new_order_items_data = [(
		order_id,
		curr_product_id,
		curr_product_quantity
	) for (curr_product_id, curr_product_quantity) in zip(product_id, product_quantity)]

	return new_order_items_data


def add_items(order_id):
	connection = connection_pool.get_connection()
	database_cursor = connection.cursor()

	try:
		new_order_items_insert_query = "INSERT INTO ORDER_ITEMS (ORDER_ID, PRODUCT_ID, PRODUCT_QUANTITY) VALUES (%s,%s,%s)"

		items_attributes = get_items_attributes(order_id)
		new_order_items_data = items_attributes

		database_cursor.executemany(new_order_items_insert_query, new_order_items_data)
		connection.commit()
	except:
		raise DatabaseError
	finally:
		database_cursor.close()
		connection.close()


def update_shipper_id(order_id):
	connection = connection_pool.get_connection()
	database_cursor = connection.cursor()

	try:
		query = 'UPDATE ORDER_HEADER SET SHIPPER_ID=%s WHERE ORDER_ID=%s;'

		shipper_id = request.get_json()['id']

		database_cursor.execute(query, (shipper_id, order_id))

		if database_cursor.rowcount == 0:
			raise NotFoundError

		connection.commit()
	except NotFoundError:
		raise NotFoundError
	except:
		raise DatabaseError
	finally:
		database_cursor.close()
		connection.close()


def update_status(order_id):
	connection = connection_pool.get_connection()
	database_cursor = connection.cursor()

	try:
		query = 'UPDATE ORDER_HEADER SET ORDER_STATUS=%s WHERE ORDER_ID=%s;'

		order_status = request.get_json()['status']

		database_cursor.execute(query, (order_status, order_id))

		if database_cursor.rowcount == 0:
			raise NotFoundError

		connection.commit()

	except NotFoundError:
		raise NotFoundError
	except:
		raise DatabaseError
	finally:
		database_cursor.close()
		connection.close()


def cancel_order(order_id):
	connection = connection_pool.get_connection()
	database_cursor = connection.cursor()

	try:
		query = 'UPDATE ORDER_HEADER SET ORDER_STATUS = %s, SHIPPER_ID = %s WHERE ORDER_ID = %s'
		database_cursor.execute(query, ('Cancelled', None, order_id))

		if database_cursor.rowcount == 0:
			raise NotFoundError

		query = 'DELETE FROM ORDER_ITEMS WHERE ORDER_ID=%s'
		database_cursor.execute(query, (order_id,))
		connection.commit()
	except:
		raise DatabaseError
	finally:
		database_cursor.close()
		connection.close()
