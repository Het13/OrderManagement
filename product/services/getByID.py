from databaseConnection import database_connection


def get_by_id(product_id):
	database, database_cursor = database_connection()

	query = 'SELECT PRODUCT_ID, PRODUCT_DESC, PRODUCT.PRODUCT_CLASS_CODE, PRODUCT_CLASS_DESC, PRODUCT_PRICE, ' \
	        'PRODUCT_QUANTITY_AVAIL, LEN, WIDTH, HEIGHT, WEIGHT FROM PRODUCT INNER JOIN PRODUCT_CLASS ON ' \
	        'PRODUCT_CLASS.PRODUCT_CLASS_CODE = PRODUCT.PRODUCT_CLASS_CODE WHERE PRODUCT_ID = %s'

	database_cursor.execute(query, (product_id,))
	data = database_cursor.fetchone()

	if data is None:
		return False

	attributes = ['id', 'product', 'class_code', 'class', 'price', 'available_quantity', 'length', 'width',
	              'height', 'weight']

	product = {}

	for i, j in zip(attributes, data):
		if j is None:
			continue
		product[i] = j
	return product
