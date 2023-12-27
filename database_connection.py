import mysql.connector
from mysql.connector import pooling

database_config = {
	'host'    : 'localhost',
	'user'    : 'root',
	'password': 'Het@2102',
	'database': 'orders1',
}

connection_pool = pooling.MySQLConnectionPool(
	pool_name='connection_pool',
	pool_size=5,
	**database_config
)
