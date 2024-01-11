from flask import request

from database_connection import connection_pool
from middleware.custom_errors import NotFoundError, DatabaseError


def to_dictionary(attributes, data):
	dictionary = {}
	for i, j in zip(attributes, data):
		if j is None:
			continue
		dictionary[i] = j

	return dictionary


def get_all():
	connection = connection_pool.get_connection()
	cursor = connection.cursor()

	try:
		category = request.args.get('category')
		if category:
			query = "SELECT product.PRODUCT_ID, product.PRODUCT_DESC, PRODUCT.PRODUCT_CLASS_CODE, " \
			        "product.PRODUCT_PRICE, product.PRODUCT_QUANTITY_AVAIL, product.LEN, " \
			        "product.WIDTH, product.HEIGHT, product.WEIGHT FROM product JOIN product_class on " \
			        "product.PRODUCT_CLASS_CODE = product_class.PRODUCT_CLASS_CODE where " \
			        "product_class.PRODUCT_CLASS_DESC = %s"
			cursor.execute(query, (category,))

		else:
			query = 'SELECT PRODUCT_ID, PRODUCT_DESC, PRODUCT.PRODUCT_CLASS_CODE, PRODUCT_CLASS_DESC, PRODUCT_PRICE, ' \
			        'PRODUCT_QUANTITY_AVAIL, LEN, WIDTH, HEIGHT, WEIGHT FROM PRODUCT INNER JOIN PRODUCT_CLASS ON ' \
			        'PRODUCT_CLASS.PRODUCT_CLASS_CODE = PRODUCT.PRODUCT_CLASS_CODE;'

			cursor.execute(query)
		data = cursor.fetchall()
		if data is None:
			raise NotFoundError

		attributes = ['id', 'product', 'class_code', 'class', 'price', 'available_quantity', 'length', 'width',
		              'height', 'weight']
		products_list = []
		for row in data:
			row_dict = to_dictionary(attributes=attributes, data=row)
			products_list.append(row_dict)

		return products_list

	except NotFoundError:
		raise NotFoundError
	except:
		raise DatabaseError
	finally:
		cursor.close()
		connection.close()


def get_by_id(product_id):
	connection = connection_pool.get_connection()
	cursor = connection.cursor()

	try:
		query = 'SELECT PRODUCT_ID, PRODUCT_DESC, PRODUCT.PRODUCT_CLASS_CODE, PRODUCT_CLASS_DESC, PRODUCT_PRICE, ' \
		        'PRODUCT_QUANTITY_AVAIL, LEN, WIDTH, HEIGHT, WEIGHT FROM PRODUCT INNER JOIN PRODUCT_CLASS ON ' \
		        'PRODUCT_CLASS.PRODUCT_CLASS_CODE = PRODUCT.PRODUCT_CLASS_CODE WHERE PRODUCT_ID = %s'

		cursor.execute(query, (product_id,))
		data = cursor.fetchone()

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
		cursor.close()
		connection.close()


def get_categories():
	connection = connection_pool.get_connection()
	cursor = connection.cursor()
	try:
		query = 'SELECT DISTINCT PRODUCT_CLASS_DESC FROM PRODUCT_CLASS'
		cursor.execute(query)
		data = cursor.fetchall()

		categories = []
		for row in data:
			categories.append(row[0])
		return categories
	except:
		raise DatabaseError
	finally:
		cursor.close()
		connection.close()
