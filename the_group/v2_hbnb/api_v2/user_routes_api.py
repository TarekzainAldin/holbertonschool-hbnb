from flask import Blueprint, request, jsonify
from models.user import User
from persistence.user_data_manager import UserDataManager
from datetime import datetime
user_bp = Blueprint('user_bp', __name__)
user_data_manager = UserDataManager()

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    required_fields = ['email', 'first_name', 'last_name']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing data'}), 400
    user = User(**data)
    result = user_data_manager.save(user)
    return jsonify(result), 201

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = user_data_manager.get_all()
    return jsonify([user.to_dict() for user in users]), 200

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_data_manager.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict()), 200

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = user_data_manager.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    for key, value in data.items():
        setattr(user, key, value)
    user.updated_at = datetime.now()
    user_data_manager.update(user)
    return jsonify(user.to_dict()), 200

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = user_data_manager.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    user_data_manager.delete(user_id)
    return '', 204
