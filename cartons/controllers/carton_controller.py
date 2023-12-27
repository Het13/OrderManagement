from flask import jsonify
from cartons.services.cartonServices import get_optimal_carton
from authorizaton import token_required, roles_required
from custom_errors import NotFoundError, DatabaseError, EmptyResult


@token_required
@roles_required('admin')
def optimal_carton(order_id):
	try:
		carton = get_optimal_carton(order_id)
		return jsonify(carton={'carton-id': carton[0], 'carton-volume': carton[1]}), 200
	except EmptyResult:
		return jsonify(failed={'message': 'No optimal carton found'}), 200
	except NotFoundError:
		return jsonify(failed={'message': f'No order with id:{order_id} found'}), 404
	except DatabaseError:
		return jsonify(failed={'message': 'Failed to fetch carton'})
