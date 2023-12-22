from databaseConnection import database_connection


def get_new_quantities(ids, quantities):
	database, database_cursor = database_connection()
	query = 'SELECT PRODUCT_QUANTITY_AVAIL FROM PRODUCT WHERE PRODUCT_ID=%s '

	original_quantities = []
	new_quantities = []

	for id in ids:
		database_cursor.execute(query, (id,))
		original_quantities.append(database_cursor.fetchone()[0])

	for new, original in zip(quantities, original_quantities):
		new_quantities.append(original - int(new))

	return new_quantities


def change_available_quantity(ids, quantities):
	database, database_cursor = database_connection()

	query = 'UPDATE PRODUCT SET PRODUCT_QUANTITY_AVAIL = %s WHERE PRODUCT_ID = %s'

	new_quantities = get_new_quantities(ids, quantities)
	for id, quantity in zip(ids, new_quantities):
		database_cursor.execute(query, (id, quantity))

	database.commit()
	database.close()

	return True




