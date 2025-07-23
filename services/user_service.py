from models.user_model import UserModel  # Correct import path
from utils.security import hash_password, check_password  # From utils module

# Create a new user
def create_user_service(data):
    hashed_password = hash_password(data['password'])  # Encrypt password before saving
    UserModel.create_user(data['name'], data['email'], hashed_password)

# Get all users
def get_all_users_service():
    return UserModel.get_all_users()

# Get a specific user by ID
def get_user_service(user_id):
    return UserModel.get_user_by_id(user_id)

# Update user information
def update_user_service(user_id, data):
    return UserModel.update_user(user_id, data)

# Delete a user
def delete_user_service(user_id):
    return UserModel.delete_user(user_id)

# Search for users by name
def search_users_service(name):
    return UserModel.search_users_by_name(name)

# Get user by email and check password
def get_user_by_email_and_password_service(email, password):
    user = UserModel.get_user_by_email(email)  # Get the user by email
    if user and check_password(user[3], password):  # Assuming user[3] is the hashed password
        return user
    return None
