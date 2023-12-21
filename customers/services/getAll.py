from databaseConnection import database_connection


def to_dict(data):
	attributes = ['id', 'first_name', 'last_name', 'email', 'phone', 'address_id', 'creation_date', 'username',
	              'gender']
	dict = {}
	for i, j in zip(attributes, data):
		dict[i] = j

	return dict


def get_all():
	database, database_cursor = database_connection()

	query = 'SELECT * FROM ONLINE_CUSTOMER'

	database_cursor.execute(query)

	customers_list = []
	for row in database_cursor.fetchall():
		row_dict = to_dict(row)
		customers_list.append(row_dict)

	return customers_list
