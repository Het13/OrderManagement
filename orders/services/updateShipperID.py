from flask import request
from databaseConnection import database_connection


def update_shipper_id(order_id):
	database, database_cursor = database_connection()

	query = 'UPDATE ORDER_HEADER SET SHIPPER_ID=%s WHERE ORDER_ID=%s;'

	shipper_id = request.form.get('id')

	database_cursor.execute(query, (shipper_id, order_id))

	if database_cursor.rowcount == 0:
		return False

	database.commit()
	database.close()

	return True
