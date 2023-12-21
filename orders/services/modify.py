from flask import request
from databaseConnection import database_connection


def is_empty_items_attributes(product_id, product_quantity):
	if product_id is None or product_id == '' \
			or product_quantity is None or product_quantity == '':
		return True
	return False


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


def modify_order(order_id):
	database, database_cursor = database_connection()

	delete_order_items_query = "DELETE FROM ORDER_ITEMS WHERE ORDER_ID = %s"
	database_cursor.execute(delete_order_items_query, (order_id,))
	if database_cursor.rowcount == 0:
		return False, f'No order with id:{order_id} found'

	new_order_items_insert_query = "INSERT INTO ORDER_ITEMS (ORDER_ID, PRODUCT_ID, PRODUCT_QUANTITY) VALUES (%s,%s,%s)"

	items_attributes = get_items_attributes(order_id)

	if not items_attributes:
		return False, 'Empty Fields'

	new_order_items_data = items_attributes

	database_cursor.executemany(new_order_items_insert_query, new_order_items_data)

	database.commit()
	database.close()

	return True, 'Successfully modified order'
