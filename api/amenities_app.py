#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
from datetime import datetime

app = Flask(__name__)
api = Api(app, version='1.0', title='Amenity API',
          description='A simple Amenity Management API')

ns = api.namespace('amenities', description='Amenity operations')

# In-memory storage
amenities = []
amenity_counter = 1

# Flask-Restx model
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='The amenity name')
})

amenity_response_model = api.model('AmenityResponse', {
    'id': fields.Integer(readonly=True, description='The unique identifier'),
    'name': fields.String(required=True, description='The amenity name'),
    'created_at': fields.DateTime(description='Creation timestamp'),
    'updated_at': fields.DateTime(description='Last updated timestamp')
})

@ns.route('/')
class AmenityList(Resource):
    @ns.doc('list_amenities')
    @ns.marshal_list_with(amenity_response_model)
    def get(self):
        '''List all amenities'''
        return amenities, 200

    @ns.doc('create_amenity')
    @ns.expect(amenity_model)
    @ns.marshal_with(amenity_response_model, code=201)
    def post(self):
        '''Create a new amenity'''
        global amenity_counter
        data = request.json
        if any(a['name'] == data['name'] for a in amenities):
            api.abort(409, "Amenity with this name already exists")
        new_amenity = {
            'id': amenity_counter,
            'name': data['name'],
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow()
        }
        amenities.append(new_amenity)
        amenity_counter += 1
        return new_amenity, 201

@ns.route('/<int:id>')
@ns.response(404, 'Amenity not found')
class Amenity(Resource):
    @ns.doc('get_amenity')
    @ns.marshal_with(amenity_response_model)
    def get(self, id):
        '''Fetch a single amenity'''
        amenity = next((a for a in amenities if a['id'] == id), None)
        if amenity is None:
            api.abort(404, "Amenity not found")
        return amenity, 200

    @ns.doc('update_amenity')
    @ns.expect(amenity_model)
    @ns.marshal_with(amenity_response_model)
    def put(self, id):
        '''Update an existing amenity'''
        amenity = next((a for a in amenities if a['id'] == id), None)
        if amenity is None:
            api.abort(404, "Amenity not found")
        data = request.json
        if any(a['name'] == data['name'] and a['id'] != id for a in amenities):
            api.abort(409, "Amenity with this name already exists")
        amenity['name'] = data['name']
        amenity['updated_at'] = datetime.utcnow()
        return amenity, 200

    @ns.doc('delete_amenity')
    @ns.response(204, 'Amenity deleted')
    def delete(self, id):
        '''Delete an amenity'''
        global amenities
        amenities = [a for a in amenities if a['id'] != id]
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)
