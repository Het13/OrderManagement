from database_connection import connection_pool
from flask import request
from datetime import datetime
from address.services import address_services
from users.services import user_services
from custom_errors import NotFoundError, DatabaseError


def get_email():
	connection = connection_pool.get_connection()
	database_cursor = connection.cursor()

	try:
		query = 'SELECT CUSTOMER_EMAIL FROM ONLINE_CUSTOMER'

		database_cursor.execute(query)
		emails = []
		for row in database_cursor.fetchall():
			emails.append(row[0])
		return emails
	except:
		raise DatabaseError
	finally:
		database_cursor.close()
		connection.close()


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
		query = 'SELECT * FROM ONLINE_CUSTOMER'

		database_cursor.execute(query)
		data = database_cursor.fetchall()

		if data is None:
			raise NotFoundError

		attributes = ['id', 'first_name', 'last_name', 'email', 'phone', 'address_id', 'creation_date', 'username',
		              'gender']
		customers_list = []
		for row in data:
			row_dict = to_dictionary(attributes=attributes, data=row)
			customers_list.append(row_dict)

		return customers_list
	except NotFoundError:
		raise NotFoundError
	except:
		raise DatabaseError
	finally:
		database_cursor.close()
		connection.close()


def get_by_id(customer_id):
	connection = connection_pool.get_connection()
	database_cursor = connection.cursor()

	try:
		query = 'SELECT * FROM ONLINE_CUSTOMER WHERE CUSTOMER_ID = %s'

		database_cursor.execute(query, (customer_id,))
		data = database_cursor.fetchone()

		if data is None:
			raise NotFoundError

		attributes = ['id', 'first_name', 'last_name', 'email', 'phone', 'address_id', 'creation_date', 'username',
		              'gender']

		customer = {}
		for i, j in zip(attributes, data):
			if j is None:
				continue
			customer[i] = j
		return customer
	except NotFoundError:
		raise NotFoundError
	except:
		raise DatabaseError
	finally:
		database_cursor.close()
		connection.close()


def get_orders(customer_id):
	connection = connection_pool.get_connection()
	database_cursor = connection.cursor()

	try:
		get_order_query = "select * from order_header where CUSTOMER_ID=%s"

		database_cursor.execute(get_order_query, (customer_id,))

		order_data = database_cursor.fetchall()

		attributes = ['id', 'customer_id', 'date', 'status', 'payment_mode', 'payment_date', 'shipment_date',
		              'shipper_id']
		orders = []
		for row in order_data:
			row_dict = to_dictionary(attributes=attributes, data=row)
			orders.append(row_dict)

		if orders == []:
			raise NotFoundError

		return orders
	except NotFoundError:
		raise NotFoundError
	except:
		raise DatabaseError
	finally:
		database_cursor.close()
		connection.close()


def get_address_id(address_data):
	try:
		address_id = address_services.add_address(address_data)
		return address_id
	except:
		raise DatabaseError


def get_attributes(request_body):
	first_name = request_body['first_name']
	last_name = request_body['last_name']
	email = request_body['email']
	phone = request_body['phone']
	address = request_body['address']
	creation_date = datetime.today().strftime('%Y-%m-%d')
	username = request_body['username']
	gender = request_body['gender']

	address_line_1 = address['address_line_1']
	address_line_2 = address['address_line_2']
	city = address['city']
	state = address['state']
	pincode = address['pincode']
	country = address['country']

	address_data = (
		address_line_1,
		address_line_2,
		city,
		state,
		pincode,
		country
	)
	try:
		address_id = get_address_id(address_data)
		new_customer_data = (
			first_name,
			last_name,
			email,
			phone,
			address_id,
			creation_date,
			username,
			gender
		)
		return new_customer_data
	except DatabaseError:
		raise DatabaseError


def add_customer():
	connection = connection_pool.get_connection()
	database_cursor = connection.cursor()
	request_body = request.get_json()
	try:
		new_customer_insert_statement = "INSERT INTO ONLINE_CUSTOMER (CUSTOMER_FNAME,CUSTOMER_LNAME,CUSTOMER_EMAIL, " \
		                                "CUSTOMER_PHONE,ADDRESS_ID,CUSTOMER_CREATION_DATE,CUSTOMER_USERNAME,CUSTOMER_GENDER) " \
		                                "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"

		new_customer_data = get_attributes(request_body)
		database_cursor.execute(new_customer_insert_statement, new_customer_data)

		customer_id = database_cursor.lastrowid

		email = request_body['email']
		password = request_body['password']

		data = {'email': email, 'password': password}
		user_services.add(data, role='user')

		connection.commit()
		return customer_id

	except:
		raise DatabaseError
	finally:
		database_cursor.close()
		connection.close()
