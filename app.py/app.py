# Import necessary modules
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Dummy user data (replace with actual data source)
users = []

# Define endpoint routes
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    # Validate input data
    if not all(key in data for key in ('email', 'first_name', 'last_name')):
        return jsonify({'error': 'Missing required fields (email, first_name, last_name)'}), 400
    
    # Check email uniqueness
    if any(user['email'] == data['email'] for user in users):
        return jsonify({'error': 'Email already exists'}), 409
    
    # Add user to the list
    user = {
        'email': data['email'],
        'first_name': data['first_name'],
        'last_name': data['last_name']
    }
    users.append(user)
    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        user.update(data)
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return '', 204

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
