from flask import Blueprint, request, jsonify
from services.user_service import create_user_service, get_all_users_service, get_user_service, update_user_service, delete_user_service, search_users_service
from utils.security import validate_user_data

user_blueprint = Blueprint('user', __name__)

# Get all users
@user_blueprint.route('/', methods=['GET'])
def get_all_users():
    users = get_all_users_service()
    return jsonify(users), 200  # 200 OK

# Get a specific user by ID
@user_blueprint.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_service(user_id)
    if user:
        return jsonify(user), 200  # 200 OK
    else:
        return jsonify({"message": "User not found"}), 404  # 404 Not Found

# Create a new user
@user_blueprint.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    if not validate_user_data(data):
        return jsonify({"message": "Invalid data"}), 400  # 400 Bad Request
    create_user_service(data)
    return jsonify({"message": "User created successfully"}), 201  # 201 Created

# Update user information
@user_blueprint.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if not validate_user_data(data):
        return jsonify({"message": "Invalid data"}), 400  # 400 Bad Request
    updated_user = update_user_service(user_id, data)
    if updated_user:
        return jsonify(updated_user), 200  # 200 OK
    else:
        return jsonify({"message": "User not found"}), 404  # 404 Not Found

# Delete a user
@user_blueprint.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if delete_user_service(user_id):
        return jsonify({"message": "User deleted successfully"}), 200  # 200 OK
    else:
        return jsonify({"message": "User not found"}), 404  # 404 Not Found

# Search users by name
@user_blueprint.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name')
    if not name:
        return jsonify({"message": "Please provide a name to search"}), 400  # 400 Bad Request
    users = search_users_service(name)
    return jsonify(users), 200  # 200 OK
