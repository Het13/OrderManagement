from flask import Blueprint
from product.controllers.product_controller import get_all, get_by_id

product_routes = Blueprint('product_routes', __name__)


product_routes.route('/api/v1/products/<int:item_id>', methods=['GET'])(get_by_id)
product_routes.route('/api/v1/products', methods=['GET'])(get_all)
