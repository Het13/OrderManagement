from databaseConnection import database_connection


def get_role(email):
	database, database_cursor = database_connection()

	query = 'SELECT ROLES FROM USERS WHERE EMAIL=%s'

	database_cursor.execute(query, (email,))

	return database_cursor.fetchone()[0]
