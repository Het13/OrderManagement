from databaseConnection import database_connection


def get_optimal_carton(order_id):
	database, database_cursor = database_connection()

	check_query = "SELECT * FROM ORDER_HEADER WHERE ORDER_ID = %s"
	database_cursor.execute(check_query, (order_id,))

	if database_cursor.fetchall() is None:
		return False

	carton_query = "SELECT CARTON.CARTON_ID, (CARTON.LEN * CARTON.WIDTH * CARTON.HEIGHT) AS CARTON_VOL FROM CARTON WHERE " \
	               "(CARTON.LEN * CARTON.WIDTH * CARTON.HEIGHT) >= (SELECT SUM(PRODUCT.LEN * PRODUCT.HEIGHT * PRODUCT.WIDTH * " \
	               "ORDER_ITEMS.PRODUCT_QUANTITY) AS PRODUCT_VOL FROM ORDER_ITEMS INNER JOIN PRODUCT ON PRODUCT.PRODUCT_ID = " \
	               "ORDER_ITEMS.PRODUCT_ID WHERE ORDER_ITEMS.ORDER_ID = %s) ORDER BY CARTON_VOL LIMIT 1;"

	carton_params = (order_id,)

	database_cursor.execute(carton_query, carton_params)

	carton = database_cursor.fetchone()
	database.close()

	return carton
