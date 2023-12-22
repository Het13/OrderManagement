from databaseConnection import database_connection


def get_email():
	database, database_cursor = database_connection()

	query = 'SELECT CUSTOMER_EMAIL FROM ONLINE_CUSTOMER'

	database_cursor.execute(query)

	return database_cursor.fetchall()
