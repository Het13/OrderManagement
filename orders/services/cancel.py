from databaseConnection import database_connection


def cancel_order(order_id):
	database, database_cursor = database_connection()

	query = 'UPDATE ORDER_HEADER SET ORDER_STATUS = %s, SHIPPER_ID = %s WHERE ORDER_ID = %s'
	database_cursor.execute(query, ('Cancelled', None, order_id))

	if database_cursor.rowcount == 0:
		return False

	query = 'DELETE FROM ORDER_ITEMS WHERE ORDER_ID=%s'
	database_cursor.execute(query, (order_id,))

	database.commit()
	database.close()

	return True
