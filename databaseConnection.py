import mysql.connector


def database_connection():
	database = mysql.connector.connect(
		host='localhost',
		user='root',
		password='Het@2102',
		database='orders'
	)
	database_cursor = database.cursor()
	return database, database_cursor


database, database_cursor = database_connection()

delete_order_items_query = "DELETE FROM ORDER_ITEMS WHERE ORDER_ID = %s"
# order_id = request.args.get('id')
order_id = 1
print(database_cursor.execute(delete_order_items_query, (order_id,)))
print(database_cursor.rowcount)
