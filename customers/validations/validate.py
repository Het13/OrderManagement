from flask import request

def check_empty_attributes():

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
	username = request.form.get('username')
	gender = request.form.get('gender')


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