from databaseConnection import database_connection
from werkzeug.security import check_password_hash
from flask import request, jsonify
import jwt
import app
import datetime


def encode_token(user):
	payload = {
		'exp'  : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
		'email': user
	}
	token = jwt.encode(payload, app.app.config['SECRET_KEY'], algorithm='HS256')
	return token


def login_user():
	auth = request.authorization
	if not auth or not auth.username or not auth.password:
		return jsonify({'message': 'Could not verify'})

	user = auth.username

	database, database_cursor = database_connection()
	query = 'SELECT PASSWORD FROM USERS WHERE EMAIL = %s'
	database_cursor.execute(query, (user,))
	password = database_cursor.fetchone()[0]

	if check_password_hash(password, auth.password):
		token = encode_token(user)
		return token
	return False
