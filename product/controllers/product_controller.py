from flask import jsonify
from product.services import product_services
from middleware.authorizaton import token_required, roles_required
from middleware.validations import check_product_category
from middleware.custom_errors import NotFoundError, DatabaseError, InvalidFilter


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
@check_product_category()
def get_all():
	try:
		products = product_services.get_all()
		print(products)
		return jsonify(success={'products': products}), 200
	except NotFoundError:
		return jsonify(failed={'message': 'No products found'})
	except DatabaseError:
		return jsonify(failed={'message': 'Failed to get products'})


@token_required
@roles_required('admin', 'user')
def get_by_category():
	try:
		products = product_services.get_by_category()
		return jsonify(success={'products': products}), 200
	except NotFoundError:
		return jsonify(failed={'message': 'No products found'})
	except DatabaseError:
		return jsonify(failed={'message': 'Failed to get products'})
