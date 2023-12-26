from flask import Blueprint
from users.controllers.userController import admin_register, login_user,change_roles

user_routes = Blueprint('user_routes', __name__)

user_routes.route('/api/v1/admin/register', methods=['POST'])(admin_register)
user_routes.route('/api/v1/users/login', methods=['POST'])(login_user)
user_routes.route('/api/v1/users/change-roles/<int:user_id>', methods=['PATCH'])(change_roles)

