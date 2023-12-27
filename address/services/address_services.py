from database_connection import connection_pool
from custom_errors import DatabaseError


def add_address(data):
	connection = connection_pool.get_connection()
	database_cursor = connection.cursor()

	try:
		new_address_insert_statement = "INSERT INTO ADDRESS(ADDRESS_LINE1, ADDRESS_LINE2, CITY, STATE, PINCODE, COUNTRY)" \
		                               " VALUES (%s, %s, %s, %s, %s, %s)"

		database_cursor.execute(new_address_insert_statement, data)
		address_id = database_cursor.lastrowid

		connection.commit()
		return address_id
	except:
		raise DatabaseError
	finally:
		database_cursor.close()
		connection.close()
