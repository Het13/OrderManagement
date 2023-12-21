from databaseConnection import database_connection

def to_dict(data):
	attributes = ['id', 'product', 'class_code', 'class', 'price', 'available_quantity', 'length', 'width',
	              'height', 'weight']
	dict = {}
	for i, j in zip(attributes, data):
		if j is None:
			continue
		dict[i] = j

	return dict
def get_all():
	database, database_cursor = database_connection()

	query = 'SELECT PRODUCT_ID, PRODUCT_DESC, PRODUCT.PRODUCT_CLASS_CODE, PRODUCT_CLASS_DESC, PRODUCT_PRICE, ' \
	        'PRODUCT_QUANTITY_AVAIL, LEN, WIDTH, HEIGHT, WEIGHT FROM PRODUCT INNER JOIN PRODUCT_CLASS ON ' \
	        'PRODUCT_CLASS.PRODUCT_CLASS_CODE = PRODUCT.PRODUCT_CLASS_CODE;'

	database_cursor.execute(query)

	products_lists = []
	for row in database_cursor.fetchall():
		row_dict = to_dict(row)
		products_lists.append(row_dict)

	return products_lists
