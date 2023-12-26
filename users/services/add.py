from databaseConnection import database_connection
from werkzeug.security import generate_password_hash


def add(data, role):
	hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
	database, database_cursor = database_connection()
	query = 'INSERT INTO USERS(EMAIL,PASSWORD,ROLES) VALUES(%s,%s,%s)'
	database_cursor.execute(query, (data['email'], hashed_password, role))
	database.commit()
	database.close()
	return True
