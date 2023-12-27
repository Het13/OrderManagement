from flask import Blueprint
from users.controllers.user_controller import admin_register, login_user,change_roles

user_routes = Blueprint('user_routes', __name__)

user_routes.route('/api/v1/admin/register', methods=['POST'])(admin_register)
user_routes.route('/api/v1/users/login', methods=['POST'])(login_user)
user_routes.route('/api/v1/users/roles/<int:user_id>', methods=['PATCH'])(change_roles)

