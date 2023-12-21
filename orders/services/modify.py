from flask import request
from databaseConnection import database_connection

def get_items_attributes(order_id):
	product_id = request.form.get('product_id')
	product_quantity = request.form.get('product_quantity')

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
		return False

	new_order_items_insert_query = "INSERT INTO ORDER_ITEMS (ORDER_ID, PRODUCT_ID, PRODUCT_QUANTITY) VALUES (%s,%s,%s)"

	items_attributes = get_items_attributes(order_id)
	new_order_items_data = items_attributes

	database_cursor.executemany(new_order_items_insert_query, new_order_items_data)

	database.commit()
	database.close()

	return True
