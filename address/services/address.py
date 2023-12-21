from databaseConnection import database_connection


def add(data):
	database, database_cursor = database_connection()

	new_address_insert_statement = "INSERT INTO ADDRESS(ADDRESS_LINE1, ADDRESS_LINE2, CITY, STATE, PINCODE, COUNTRY)" \
	                               " VALUES (%s, %s, %s, %s, %s, %s)"

	database_cursor.execute(new_address_insert_statement, data)

	address_id = database_cursor.lastrowid

	database.commit()
	database.close()

	return address_id
