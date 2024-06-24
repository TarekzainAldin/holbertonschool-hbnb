from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource, fields
from models.user import User
from persistence.file_storage import FileStorage
from datetime import datetime
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
ns = api.namespace('users', description='User operations')
user_model = ns.model('User', {
    'id': fields.String(readOnly=True, description='The unique identifier of a user'),
    'email': fields.String(required=True, description='The email of the user'),
    'first_name': fields.String(required=True, description='The first name of the user'),
    'last_name': fields.String(required=True, description='The last name of the user'),
    'created_at': fields.String(readOnly=True, description='The time the user was created'),
    'updated_at': fields.String(readOnly=True, description='The last time the user was updated'),
})
storage = FileStorage()
@ns.route('/')
class UserList(Resource):
    @ns.doc('list_users')
    @ns.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        users = storage.get_all('User')
        return users, 200
    @ns.doc('create_user')
    @ns.expect(user_model)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        """Create a new user"""
        data = request.json
        if not data.get('email') or not data.get('first_name') or not data.get('last_name'):
            return {'message': 'Missing required fields'}, 400
        if '@' not in data['email']:
            return {'message': 'Invalid email format'}, 400
        existing_users = storage.get_all('User')
        if any(user['email'] == data['email'] for user in existing_users):
            return {'message': 'Email already exists'}, 409
        new_user = User(email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
        storage.save(new_user)
        return new_user.to_dict(), 201
@ns.route('/<string:id>')
@ns.response(404, 'User not found')
@ns.param('id', 'The user identifier')
class User(Resource):
    @ns.doc('get_user')
    @ns.marshal_with(user_model)
    def get(self, id):
        """Fetch a user given its identifier"""
        user = storage.get(id, 'User')
        if user:
            return user, 200
        return {'message': 'User not found'}, 404
    @ns.doc('update_user')
    @ns.expect(user_model)
    @ns.marshal_with(user_model)
    def put(self, id):
        """Update a user given its identifier"""
        data = request.json
        if not data.get('email') or not data.get('first_name') or not data.get('last_name'):
            return {'message': 'Missing required fields'}, 400
        if '@' not in data['email']:
            return {'message': 'Invalid email format'}, 400
        user = storage.get(id, 'User')
        if not user:
            return {'message': 'User not found'}, 404
        user.email = data['email']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.updated_at = datetime.now()
        storage.save(user)
        return user.to_dict(), 200
    @ns.doc('delete_user')
    @ns.response(204, 'User deleted')
    def delete(self, id):
        """Delete a user given its identifier"""
        user = storage.get(id, 'User')
        if not user:
            return {'message': 'User not found'}, 404
        storage.delete(id, 'User')
        return '', 204
api.add_namespace(ns, path='/users')
