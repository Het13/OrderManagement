from functools import wraps
from flask import request, jsonify
from customers.services.customer_services import get_email


def validate_request_body(required_fields):
	def decorator(f):
		@wraps(f)
		def wrapper(*args, **kwargs):
			if not request.is_json:
				return jsonify(error={'message': 'Invalid request type'})

			request_body = request.get_json()
			for field in required_fields:
				if field not in request_body or request_body[field] == "":
					return jsonify(error={'Failed': 'Empty Fields'})

			return f(*args, **kwargs)

		return wrapper

	return decorator


def check_duplicate_email():
	def decorator(f):
		@wraps(f)
		def wrapper(*args, **kwargs):
			request_body = request.get_json()
			if request_body['email'] in get_email():
				return jsonify(error={'message': 'Duplicate email'})
			return f(*args, **kwargs)

		return wrapper

	return decorator
