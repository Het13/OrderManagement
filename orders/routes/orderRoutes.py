from flask import Blueprint
from orders.controllers.orderController import add_order, modify_order, update_status, update_shipper_id

order_routes = Blueprint('order_routes', __name__)

order_routes.route('/api/v1/orders/new', methods=['POST'])(add_order)
order_routes.route('/api/v1/orders/modify/<int:order_id>', methods=['POST'])(modify_order)
order_routes.route('/api/v1/orders/<int:order_id>/status/', methods=['PATCH'])(update_status)
order_routes.route('/api/v1/orders/<int:order_id>/shipper-id', methods=['PATCH'])(update_shipper_id)
