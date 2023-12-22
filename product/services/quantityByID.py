from databaseConnection import database_connection


def quantity_available(product_id):
	database, database_cursor = database_connection()
	query = 'SELECT PRODUCT_QUANTITY_AVAIL FROM PRODUCT WHERE PRODUCT_ID=%s'
	database_cursor.execute(query, (product_id,))
	return database_cursor.fetchone()[0]