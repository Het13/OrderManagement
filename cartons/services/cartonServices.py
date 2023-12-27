from database_connection import connection_pool
from custom_errors import NotFoundError, DatabaseError, EmptyResult


def get_optimal_carton(order_id):
	connection = connection_pool.get_connection()
	database_cursor = connection.cursor()

	try:
		check_query = "SELECT * FROM ORDER_HEADER WHERE ORDER_ID = %s"
		database_cursor.execute(check_query, (order_id,))

		if database_cursor.fetchall() is None:
			raise NotFoundError

		carton_query = "SELECT CARTON.CARTON_ID, (CARTON.LEN * CARTON.WIDTH * CARTON.HEIGHT) AS CARTON_VOL FROM CARTON WHERE " \
		               "(CARTON.LEN * CARTON.WIDTH * CARTON.HEIGHT) >= (SELECT SUM(PRODUCT.LEN * PRODUCT.HEIGHT * PRODUCT.WIDTH * " \
		               "ORDER_ITEMS.PRODUCT_QUANTITY) AS PRODUCT_VOL FROM ORDER_ITEMS INNER JOIN PRODUCT ON PRODUCT.PRODUCT_ID = " \
		               "ORDER_ITEMS.PRODUCT_ID WHERE ORDER_ITEMS.ORDER_ID = %s) ORDER BY CARTON_VOL LIMIT 1;"

		carton_params = (order_id,)

		database_cursor.execute(carton_query, carton_params)

		carton = database_cursor.fetchone()

		if carton is None:
			raise EmptyResult
		return carton
	except NotFoundError:
		raise NotFoundError
	except:
		raise DatabaseError
	finally:
		database_cursor.close()
		connection.close()
