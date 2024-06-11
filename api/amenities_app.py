from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource, fields
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///amenities.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app, version='1.0', title='Amenity Management API', description='A simple Amenity Management API')

# Initialize Flask-Restx Namespace
ns = api.namespace('amenities', description='Amenities operations')

class Amenity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Amenity {self.name}>'

db.create_all()

# Define the expected model for POST and PUT requests
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='The amenity name')
})

@ns.route('/')
class AmenityList(Resource):
    @ns.doc('list_amenities')
    @ns.marshal_list_with(amenity_model)
    def get(self):
        """List all amenities"""
        amenities = Amenity.query.all()
        return amenities, 200

    @ns.doc('create_amenity')
    @ns.expect(amenity_model)
    @ns.response(201, 'Amenity created successfully')
    @ns.response(400, 'Invalid input')
    @ns.response(409, 'Amenity already exists')
    def post(self):
        """Create a new amenity"""
        data = request.json
        if 'name' not in data or not data['name'].strip():
            return {'message': 'Amenity name is required and cannot be empty'}, 400

        if Amenity.query.filter_by(name=data['name']).first():
            return {'message': 'Amenity already exists'}, 409

        new_amenity = Amenity(name=data['name'])
        db.session.add(new_amenity)
        db.session.commit()
        return {'message': 'Amenity created successfully'}, 201

@ns.route('/<int:amenity_id>')
@ns.response(404, 'Amenity not found')
class AmenityResource(Resource):
    @ns.doc('get_amenity')
    @ns.marshal_with(amenity_model)
    def get(self, amenity_id):
        """Fetch an amenity given its identifier"""
        amenity = Amenity.query.get_or_404(amenity_id)
        return amenity, 200

    @ns.doc('update_amenity')
    @ns.expect(amenity_model)
    @ns.response(200, 'Amenity updated successfully')
    @ns.response(400, 'Invalid input')
    @ns.response(404, 'Amenity not found')
    @ns.response(409, 'Amenity already exists')
    def put(self, amenity_id):
        """Update an existing amenity"""
        data = request.json
        if 'name' not in data or not data['name'].strip():
            return {'message': 'Amenity name is required and cannot be empty'}, 400

        amenity = Amenity.query.get_or_404(amenity_id)

        if Amenity.query.filter(Amenity.name == data['name'], Amenity.id != amenity_id).first():
            return {'message': 'Amenity already exists'}, 409

        amenity.name = data['name']
        db.session.commit()
        return {'message': 'Amenity updated successfully'}, 200

    @ns.doc('delete_amenity')
    @ns.response(204, 'Amenity deleted successfully')
    @ns.response(404, 'Amenity not found')
    def delete(self, amenity_id):
        """Delete an amenity given its identifier"""
        amenity = Amenity.query.get_or_404(amenity_id)
        db.session.delete(amenity)
        db.session.commit()
        return '', 204
