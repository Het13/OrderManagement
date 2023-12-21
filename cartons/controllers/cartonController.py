from flask import jsonify
from cartons.services.optimal import get_optimal_carton


def optimal_carton(order_id):
	result = get_optimal_carton(order_id)
	if not result:
		return jsonify(response={'message': f'No order with id:{order_id} found'}), 404
	carton = result
	return jsonify(carton={'carton-id': carton[0], 'carton-volume': carton[1]}), 200
