from databaseConnection import database_connection


def get_user_ids():
	database, database_cursor = database_connection()

	query = 'SELECT ID FROM USERS'
	database_cursor.execute(query)
	users = []
	for row in database_cursor.fetchall():
		users.append(row[0])
	database.close()

	return users
