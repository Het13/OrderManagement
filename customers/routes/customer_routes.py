from flask import Blueprint
from customers.controllers.customer_controller import add_customer, get_by_id, get_all, get_orders

customer_routes = Blueprint('customer_routes', __name__)

customer_routes.route('/api/v1/customers', methods=['POST'])(add_customer)
customer_routes.route('/api/v1/customers/<int:id>', methods=['GET'])(get_by_id)
customer_routes.route('/api/v1/customers', methods=['GET'])(get_all)
customer_routes.route('/api/v1/customers/<int:id>/orders', methods=['GET'])(get_orders)
