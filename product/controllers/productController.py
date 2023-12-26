from flask import jsonify
from product.services import getByID, getAll
from authorizaton import token_required, roles_required


@token_required
@roles_required('admin','user')
def get_by_id(item_id):
	product_details = getByID.get_by_id(item_id)
	if not product_details:
		return jsonify(failed={'message': f'No product with id: {item_id} found'}), 200
	return jsonify(product=product_details), 200


@token_required
@roles_required('admin', 'user')
def get_all():
	return jsonify(all_products=getAll.get_all()), 200
