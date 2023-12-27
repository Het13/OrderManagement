from flask import Blueprint
from orders.controllers.order_controller import add_order, add_items, update_status, update_shipper_id,cancel_order

order_routes = Blueprint('order_routes', __name__)

order_routes.route('/api/v1/customers/<int:id>/orders', methods=['POST'])(add_order)
order_routes.route('/api/v1/orders/<int:order_id>/lineitems', methods=['POST'])(add_items)
order_routes.route('/api/v1/orders/<int:order_id>/status/', methods=['PATCH'])(update_status)
order_routes.route('/api/v1/orders/<int:order_id>/shipper-id', methods=['PATCH'])(update_shipper_id)
order_routes.route('/api/v1/orders/<int:order_id>', methods=['DELETE'])(cancel_order)
