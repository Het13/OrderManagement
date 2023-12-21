from flask import Blueprint
from orders.controllers.orderController import add_order, modify_order

order_routes = Blueprint('order_routes', __name__)

order_routes.route('/api/v1/orders/new', methods=['POST'])(add_order)
order_routes.route('/api/v1/orders/modify/<int:order_id>', methods=['POST'])(modify_order)