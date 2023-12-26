from flask import Flask
from cartons.routes.cartonRoutes import carton_routes
from orders.routes.orderRoutes import order_routes
from customers.routes.customerRoutes import customer_routes
from product.routes.productRoutes import product_routes
from address.routes.addressRoutes import address_routes
from users.routes.userRoutes import user_routes

app = Flask(__name__)
app.config.from_object('config')
app.json.sort_keys = False


app.register_blueprint(carton_routes, url_prefix='/')
app.register_blueprint(order_routes, url_prefix='/')
app.register_blueprint(customer_routes, url_prefix='/')
app.register_blueprint(product_routes, url_prefix='/')
app.register_blueprint(address_routes, url_prefix='/')
app.register_blueprint(user_routes, url_prefix='/')

if __name__ == '__main__':
	app.run(debug=True)
