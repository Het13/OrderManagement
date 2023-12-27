from database_connection import connection_pool
from custom_errors import NotFoundError, DatabaseError


def to_dictionary(attributes, data):
	dictionary = {}
	for i, j in zip(attributes, data):
		if j is None:
			continue
		dictionary[i] = j

	return dictionary


def get_all():
	connection = connection_pool.get_connection()
	database_cursor = connection.cursor()

	try:
		query = 'SELECT PRODUCT_ID, PRODUCT_DESC, PRODUCT.PRODUCT_CLASS_CODE, PRODUCT_CLASS_DESC, PRODUCT_PRICE, ' \
		        'PRODUCT_QUANTITY_AVAIL, LEN, WIDTH, HEIGHT, WEIGHT FROM PRODUCT INNER JOIN PRODUCT_CLASS ON ' \
		        'PRODUCT_CLASS.PRODUCT_CLASS_CODE = PRODUCT.PRODUCT_CLASS_CODE;'

		database_cursor.execute(query)

		data = database_cursor.fetchall()
		if data is None:
			raise NotFoundError

		attributes = ['id', 'product', 'class_code', 'class', 'price', 'available_quantity', 'length', 'width',
		              'height', 'weight']
		products_lists = []
		for row in data:
			row_dict = to_dictionary(attributes=attributes, data=row)
			products_lists.append(row_dict)

		return products_lists

	except NotFoundError:
		raise NotFoundError
	except:
		raise DatabaseError
	finally:
		database_cursor.close()
		connection.close()


def get_by_id(product_id):
	connection = connection_pool.get_connection()
	database_cursor = connection.cursor()

	try:
		query = 'SELECT PRODUCT_ID, PRODUCT_DESC, PRODUCT.PRODUCT_CLASS_CODE, PRODUCT_CLASS_DESC, PRODUCT_PRICE, ' \
		        'PRODUCT_QUANTITY_AVAIL, LEN, WIDTH, HEIGHT, WEIGHT FROM PRODUCT INNER JOIN PRODUCT_CLASS ON ' \
		        'PRODUCT_CLASS.PRODUCT_CLASS_CODE = PRODUCT.PRODUCT_CLASS_CODE WHERE PRODUCT_ID = %s'

		database_cursor.execute(query, (product_id,))
		data = database_cursor.fetchone()

		if data is None:
			raise NotFoundError

		attributes = ['id', 'product', 'class_code', 'class', 'price', 'available_quantity', 'length', 'width',
		              'height', 'weight']

		product = to_dictionary(attributes=attributes, data=data)
		return product
	except NotFoundError:
		raise NotFoundError
	except:
		raise DatabaseError
	finally:
		database_cursor.close()
		connection.close()
