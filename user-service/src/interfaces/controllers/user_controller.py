# user_controller.py
from flask import Blueprint, request, jsonify
from application.user_service import UserService

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()

@user_controller.route('/users', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    full_name = data.get('full_name')
    user = user_service.create_user(username, email, full_name)
    return jsonify({'message': 'User created successfully', 'user': user.__dict__}), 201

@user_controller.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify(user.__dict__)
    return jsonify({'message': 'User not found'}), 404

@user_controller.route('/users', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    return jsonify([user.__dict__ for user in users])

@user_controller.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    username = data.get('username')
    email = data.get('email')
    full_name = data.get('full_name')
    user = user_service.update_user(user_id, username, email, full_name)
    return jsonify({'message': 'User updated successfully', 'user': user.__dict__})

@user_controller.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_service.delete_user(user_id)
    return jsonify({'message': 'User deleted successfully'})
