import mysql.connector


def database_connection():
	database = mysql.connector.connect(
		host='localhost',
		user='root',
		password='Het@2102',
		database='orders1'
	)
	database_cursor = database.cursor()
	return database, database_cursor
