from flask import Flask
from cartons.routes.cartonRoutes import carton_routes
from orders.routes.order_routes import order_routes
from customers.routes.customer_routes import customer_routes
from product.routes.product_routes import product_routes
from address.routes.address_routes import address_routes
from users.routes.user_routes import user_routes

app = Flask(__name__)
app.config.from_object('config')
app.json.sort_keys = False

# Routes Registration
app.register_blueprint(carton_routes, url_prefix='/')
app.register_blueprint(order_routes, url_prefix='/')
app.register_blueprint(customer_routes, url_prefix='/')
app.register_blueprint(product_routes, url_prefix='/')
app.register_blueprint(address_routes, url_prefix='/')
app.register_blueprint(user_routes, url_prefix='/')

if __name__ == '__main__':
	app.run()
