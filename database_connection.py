from mysql.connector import pooling
from dotenv import load_dotenv
import os

load_dotenv('.env')

# database configuration
database_config = {
	'host'    : os.environ.get('HOST'),
	'user'    : os.environ.get('USER'),
	'password': os.environ.get('PASSWORD'),
	'database': os.environ.get('DATABASE')
}

# creating database connection pool
connection_pool = pooling.MySQLConnectionPool(
	pool_name='connection_pool',
	pool_size=5,
	**database_config
)
