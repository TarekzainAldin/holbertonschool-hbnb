from flask import Flask, jsonify, request
from models.user import User

app = Flask(__name__)

# Dummy user data
users = []

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    # Validate required fields
    if 'email' not in data or 'first_name' not in data or 'last_name' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    email = data['email']
    if not email or '@' not in email or '.' not in email:
        return jsonify({'error': 'Invalid email format'}), 400

    if any(user.email == email for user in users):
        return jsonify({'error': 'Email already exists'}), 409

    # Create a new user
    user = User(email=email, first_name=data['first_name'], last_name=data['last_name'])
    users.append(user)
    
    return jsonify({'message': 'User created successfully', 'user': user.__dict__}), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': [user.__dict__ for user in users]}), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user.id == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'user': user.__dict__}), 200

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    user = next((user for user in users if user.id == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Validate required fields
    if 'email' in data and ('@' not in data['email'] or '.' not in data['email']):
        return jsonify({'error': 'Invalid email format'}), 400

    if 'email' in data and data['email'] != user.email and any(u.email == data['email'] for u in users):
        return jsonify({'error': 'Email already exists'}), 409

    # Update user data
    if 'email' in data:
        user.email = data['email']
    if 'first_name' in data:
        user.first_name = data['first_name']
    if 'last_name' in data:
        user.last_name = data['last_name']

    return jsonify({'message': 'User updated successfully', 'user': user.__dict__}), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((user for user in users if user.id == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    users.remove(user)
    return jsonify({'message': 'User deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
