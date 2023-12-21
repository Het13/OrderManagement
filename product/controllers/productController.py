from flask import jsonify
from product.services import getByID, getAll


def get_by_id(id):
	result = getByID.get_by_id(id)
	if not result:
		return jsonify(failed={'message': f'No product with id: {id} found'}), 200
	return jsonify(customer=result), 200


def get_all():
	return jsonify(all_products=getAll.get_all()), 200
