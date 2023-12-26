from databaseConnection import database_connection


def change_roles(new_role, user_id):
	database, database_cursor = database_connection()
	query = 'UPDATE USERS SET ROLES=%s WHERE ID=%s'
	database_cursor.execute(query, (new_role, user_id))
	database.commit()
	database.close()
	return
