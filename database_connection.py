from mysql.connector import pooling

# databse configuration
database_config = {
	'host'    : 'localhost',
	'user'    : 'root',
	'password': 'Het@2102',
	'database': 'orders1',
}

# creating database connection pool
connection_pool = pooling.MySQLConnectionPool(
	pool_name='connection_pool',
	pool_size=5,
	**database_config
)
