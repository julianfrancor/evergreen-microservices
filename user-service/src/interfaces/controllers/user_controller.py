# user_controller.py
from flask import Blueprint, request, jsonify
from application.user_service import UserService

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()

@user_controller.route('/users', methods=['POST'])
def create_user():
    username = request.json.get('username')
    email = request.json.get('email')
    full_name = request.json.get('full_name')
    # Validate input data here, and return a response with an error message if validation fails.
    if not username or not email or not full_name:
        return jsonify({'error': 'Missing required fields'}), 400
    # Try to create the user
    user = user_service.create_user(username, email, full_name)
    # Check if user creation was successful
    if user:
        return jsonify({'message': 'User created successfully', 'user': user.__dict__}), 201
    else:
        return jsonify({'error': 'User creation failed'}), 500

@user_controller.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user == None:
        return jsonify({'message': 'User not found'}), 404
    user_dict = [user.to_dict()]
    if user_dict:
        return jsonify(user_dict)
    return jsonify({'message': 'User not found'}), 404

@user_controller.route('/users', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    user_dicts = [user.to_dict() for user in users]
    print(user_dicts)
    return jsonify(user_dicts), 200


@user_controller.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    username = data.get('username')
    email = data.get('email')
    full_name = data.get('full_name')
    user = user_service.update_user(user_id, username, email, full_name)
    if user == None:
        jsonify({'error': 'User update failed'}), 500
    user_element = [user.to_dict()]
    if user_element:
        return jsonify({'message': 'User updated successfully', 'user': user_element}), 201
    else:
        return jsonify({'error': 'User update failed'}), 500

@user_controller.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_service.delete_user(user_id)
    return jsonify({'message': 'User deleted successfully'})
