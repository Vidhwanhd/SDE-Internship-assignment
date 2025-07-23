from flask import Blueprint, request, jsonify
from services.user_service import get_user_by_email_and_password_service

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400  # 400 Bad Request

    user = get_user_by_email_and_password_service(email, password)

    if user:
        return jsonify({"status": "success", "user_id": user[0]}), 200  # 200 OK
    else:
        return jsonify({"status": "failed", "message": "Invalid email or password"}), 401  # 401 Unauthorized
