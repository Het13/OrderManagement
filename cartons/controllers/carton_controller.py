from flask import jsonify
from cartons.services.cartonServices import get_optimal_carton
from middleware.authorizaton import token_required, roles_required
from middleware.custom_errors import NotFoundError, DatabaseError, EmptyResult


@token_required
@roles_required('admin')
def optimal_carton(order_id):
	try:
		carton = get_optimal_carton(order_id)
		return jsonify(success={'carton': {'id': carton['id'], 'volume': carton['volume']}}), 200
	except EmptyResult:
		return jsonify(failed={'message': 'No optimal carton found'}), 200
	except NotFoundError:
		return jsonify(failed={'message': 'Order not found'}), 404
	except DatabaseError:
		return jsonify(failed={'message': 'Failed to fetch carton'})
