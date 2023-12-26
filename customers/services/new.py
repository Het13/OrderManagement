from flask import request
from datetime import datetime
from databaseConnection import database_connection
from address.services import address
from users.services.add import add


def get_address_id(address_data):
	address_id = address.add(address_data)

	return address_id


def get_attributes():
	first_name = request.form.get('first_name')
	last_name = request.form.get('last_name')
	email = request.form.get('email')
	phone = request.form.get('phone')
	address_line_1 = request.form.get('address_line_1')
	address_line_2 = request.form.get('address_line_2')
	city = request.form.get('city')
	state = request.form.get('state')
	pincode = request.form.get('pincode')
	country = request.form.get('country')
	creation_date = datetime.today().strftime('%Y-%m-%d')
	username = request.form.get('username')
	gender = request.form.get('gender')

	address = (
		address_line_1,
		address_line_2,
		city,
		state,
		pincode,
		country
	)

	address_id = get_address_id(address)

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


def add_customer():
	database, database_cursor = database_connection()
	new_customer_insert_statement = "INSERT INTO ONLINE_CUSTOMER (CUSTOMER_FNAME,CUSTOMER_LNAME,CUSTOMER_EMAIL, " \
	                                "CUSTOMER_PHONE,ADDRESS_ID,CUSTOMER_CREATION_DATE,CUSTOMER_USERNAME,CUSTOMER_GENDER) " \
	                                "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"

	new_customer_data = get_attributes()
	database_cursor.execute(new_customer_insert_statement, new_customer_data)

	customer_id = database_cursor.lastrowid
	database.commit()
	database.close()

	email = request.form.get('email')
	password = request.form.get('password')

	data = {'email': email, 'password': password}
	add(data, role='user')

	return customer_id
