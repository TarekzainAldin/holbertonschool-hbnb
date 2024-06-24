import os
import sys

# Add the parent directory of 'api' to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
from models.user import User
from persistence.data_manager import DataManager

app = Flask(__name__)
api = Api(app, doc='/docs')
data_manager = DataManager()

user_model = api.model('User', {
    'email': fields.String(required=True, description='User email'),
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name')
})

@api.route('/users')
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        return [user.to_dict() for user in data_manager.users]

    @api.expect(user_model)
    @api.response(201, 'User created successfully')
    @api.response(400, 'Invalid input')
    @api.response(409, 'Email already exists')
    def post(self):
        data = request.get_json()
        if not data:
            api.abort(400, 'No data provided')
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        if not email or '@' not in email or '.' not in email:
            api.abort(400, 'Invalid email format')
        if not first_name or not isinstance(first_name, str):
            api.abort(400, 'Invalid first name')
        if not last_name or not isinstance(last_name, str):
            api.abort(400, 'Invalid last name')
        if any(user.email == email for user in data_manager.users):
            api.abort(409, 'Email already exists')
        user = User(email=email, first_name=first_name, last_name=last_name)
        data_manager.save(user)
        return {'message': 'User created successfully', 'user': user.to_dict()}, 201

@api.route('/users/<int:user_id>')
class UserDetail(Resource):
    @api.marshal_with(user_model)
    @api.response(200, 'Success')
    @api.response(404, 'User not found')
    def get(self, user_id):
        user = data_manager.get(user_id, 'user')
        if not user:
            api.abort(404, 'User not found')
        return user.to_dict()

    @api.expect(user_model)
    @api.response(200, 'User updated successfully')
    @api.response(400, 'Invalid input')
    @api.response(404, 'User not found')
    @api.response(409, 'Email already exists')
    def put(self, user_id):
        data = request.get_json()
        if not data:
            api.abort(400, 'No data provided')
        user = data_manager.get(user_id, 'user')
        if not user:
            api.abort(404, 'User not found')
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        if email:
            if '@' not in email or '.' not in email:
                api.abort(400, 'Invalid email format')
            if any(u.email == email and u.id != user_id for u in data_manager.users):
                api.abort(409, 'Email already exists')
            user.email = email
        if first_name:
            if not isinstance(first_name, str):
                api.abort(400, 'Invalid first name')
            user.first_name = first_name
        if last_name:
            if not isinstance(last_name, str):
                api.abort(400, 'Invalid last name')
            user.last_name = last_name
        data_manager.update(user)
        return {'message': 'User updated successfully', 'user': user.to_dict()}

    @api.response(204, 'User deleted successfully')
    @api.response(404, 'User not found')
    def delete(self, user_id):
        user = data_manager.get(user_id, 'user')
        if not user:
            api.abort(404, 'User not found')
        data_manager.delete(user_id, 'user')
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)
