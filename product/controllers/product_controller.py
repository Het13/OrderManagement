from flask import jsonify
from product.services import product_services
from authorizaton import token_required, roles_required
from custom_errors import NotFoundError, DatabaseError


@token_required
@roles_required('admin', 'user')
def get_by_id(item_id):
	try:
		product_details = product_services.get_by_id(item_id)
		return jsonify(success={'product': product_details}), 200
	except NotFoundError:
		return jsonify(failed={'message': 'Product not found'}), 200
	except DatabaseError:
		return jsonify(failed={'message': 'Failed to get product'})


@token_required
@roles_required('admin', 'user')
def get_all():
	try:
		all_products = product_services.get_all()
		return jsonify(success={'all_products': all_products}), 200
	except NotFoundError:
		return jsonify(failed={'message': 'No products found'})
	except DatabaseError:
		return jsonify(failed={'message': 'Failed to get products'})
