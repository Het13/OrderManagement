from databaseConnection import database_connection


def to_dict(data):
	attributes = ['id', 'customer_id', 'date', 'status', 'payment_mode', 'payment_date', 'shipment_date', 'shipper_id']
	dict = {}
	for i, j in zip(attributes, data):
		dict[i] = j

	return dict


def get_orders(customer_id):
	database, database_cursor = database_connection()
	get_order_query = "select * from order_header where CUSTOMER_ID=%s"

	database_cursor.execute(get_order_query, (customer_id,))

	order_data = database_cursor.fetchall()
	if order_data is None:
		return False, f'No customer with id: {customer_id} found'

	orders = []
	for row in order_data:
		row_dict = to_dict(row)
		orders.append(row_dict)

	return True, orders
