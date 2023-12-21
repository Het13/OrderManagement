from databaseConnection import database_connection


def get_by_id(customer_id):
	database, database_cursor = database_connection()

	query = 'SELECT * FROM ONLINE_CUSTOMER WHERE CUSTOMER_ID = %s'

	database_cursor.execute(query, (customer_id,))
	data = database_cursor.fetchone()

	if data is None:
		return False

	attributes = ['id', 'first_name', 'last_name', 'email', 'phone', 'address_id', 'creation_date', 'username',
	                       'gender']

	customer = {}

	for i, j in zip(attributes, data):
		customer[i] = j
	return customer
