from flask import Blueprint
from cartons.controllers.carton_controller import optimal_carton

carton_routes = Blueprint('carton_routes', __name__)

carton_routes.route('/api/v1/cartons/optimal/<int:order_id>', methods=['GET'])(optimal_carton)
