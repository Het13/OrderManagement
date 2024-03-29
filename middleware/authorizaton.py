from functools import wraps
import jwt
from flask import request, jsonify
import app

from users.services.user_services import get_role
from middleware.custom_errors import DatabaseError


# decorator for validating JWT Token
def token_required(f):
	@wraps(f)
	def decorator(*args, **kwargs):
		token = None
		if 'Authorization' in request.headers:
			token = request.headers.get('Authorization')
		if not token:
			return jsonify(failed={'message': 'Authorization missing'}), 401
		try:
			data = jwt.decode(token, app.app.config['SECRET_KEY'], algorithms=['HS256'])
		except jwt.ExpiredSignatureError:
			return jsonify(failed={'message': 'Token has expired'}), 401
		except jwt.InvalidTokenError:
			return jsonify(failed={'message': 'Invalid token'}), 401
		except:
			return jsonify(error={'error': 'An error occurred'}), 500

		return f(*args, **kwargs)

	return decorator


# decorator for Role Based Authorization
def roles_required(*roles):
	def wrapper(f):
		@wraps(f)
		def decorator(*args, **kwargs):
			token = request.headers.get('Authorization')
			data = jwt.decode(token, app.app.config['SECRET_KEY'], algorithms=['HS256'])
			email = data['email']
			try:
				role = get_role(email)
				if role not in roles:
					return jsonify(failed={'message': 'You are not authorized'}), 403
			except DatabaseError:
				return jsonify(failed={'message': 'Authorization Failed'})

			return f(*args, **kwargs)

		return decorator

	return wrapper
