from flask import Flask, request, jsonify
from models.user import User
from persistence.data_manager import DataManager
from api.amenity_routes_api import amenity_bp
from flask_restx import Api

import re
from datetime import datetime

app = Flask(__name__)
app.register_blueprint(amenity_bp)

data_manager = DataManager()

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or not all(key in data for key in ("email", "first_name", "last_name")):
        return jsonify({"error": "Invalid input"}), 400

    if not is_valid_email(data["email"]):
        return jsonify({"error": "Invalid email format"}), 400

    existing_users = data_manager.data.get("User", [])
    if any(user.email == data["email"] for user in existing_users):
        return jsonify({"error": "Email already exists"}), 409

    user = User(email=data["email"], first_name=data["first_name"], last_name=data["last_name"])
    result = data_manager.save(user)
    return jsonify(result), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = data_manager.data.get("User", [])
    return jsonify([user.to_dict() for user in users]), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = data_manager.get(user_id, "User")
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = data_manager.get(user_id, "User")
    if user is None:
        return jsonify({"error": "User not found"}), 404

    if "email" in data:
        if not is_valid_email(data["email"]):
            return jsonify({"error": "Invalid email format"}), 400
        if any(existing_user.email == data["email"] for existing_user in data_manager.data.get("User", []) if existing_user.id != user_id):
            return jsonify({"error": "Email already exists"}), 409
        user.email = data["email"]
    if "first_name" in data:
        if not isinstance(data["first_name"], str) or not data["first_name"]:
            return jsonify({"error": "Invalid first name"}), 400
        user.first_name = data["first_name"]
    if "last_name" in data:
        if not isinstance(data["last_name"], str) or not data["last_name"]:
            return jsonify({"error": "Invalid last name"}), 400
        user.last_name = data["last_name"]

    user.updated_at = datetime.now()

    if data_manager.update(user):
        return jsonify(user.to_dict()), 200
    return jsonify({"error": "Failed to update user"}), 400

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if data_manager.delete(user_id, "User"):
        return '', 204
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
