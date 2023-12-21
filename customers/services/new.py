from flask import request
from datetime import datetime
from databaseConnection import database_connection
from address.services import address

def check_empty_attributes(first_name, last_name, email, phone, address_line_1, address_line_2, city, state, pincode,
                           country, username, gender):
	if first_name is None or first_name == '' \
			or last_name is None or last_name == '' \
			or email is None or email == '' \
			or phone is None or phone == '' \
			or address_line_1 is None or address_line_1 == '' \
			or address_line_2 is None or address_line_2 == '' \
			or city is None or city == '' \
			or state is None or state == '' \
			or pincode is None or pincode == '' \
			or country is None or pincode == '' \
			or username is None or username == '' \
			or gender is None or gender == '':
		return True
	return False


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

	if check_empty_attributes(first_name, last_name, email, phone, address_line_1, address_line_2, city, state, pincode,
	                          country, username, gender):
		return False

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

	if not get_attributes():
		return False

	new_customer_data = get_attributes()
	database_cursor.execute(new_customer_insert_statement, new_customer_data)

	customer_id = database_cursor.lastrowid
	database.commit()
	database.close()

	return customer_id
