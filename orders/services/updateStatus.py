from flask import request
from databaseConnection import database_connection


def update_status(order_id):
	database, database_cursor = database_connection()

	query = 'UPDATE ORDER_HEADER SET ORDER_STATUS=%s WHERE ORDER_ID=%s;'

	order_status = request.form.get('status')

	database_cursor.execute(query, (order_status, order_id))

	if database_cursor.rowcount == 0:
		return False

	database.commit()
	database.close()

	return True
