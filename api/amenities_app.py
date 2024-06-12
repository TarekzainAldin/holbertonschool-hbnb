from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from datetime import datetime

app = Flask(__name__)
api = Api(app, version='1.0', title='Amenity Management API', description='A simple Amenity Management API')

# Initialize Flask-Restx Namespace
ns = api.namespace('amenities', description='Amenities operations')

# In-memory data structure to store amenities
amenities = {}
amenity_counter = 1

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
        return list(amenities.values()), 200

    @ns.doc('create_amenity')
    @ns.expect(amenity_model)
    @ns.response(201, 'Amenity created successfully')
    @ns.response(400, 'Invalid input')
    @ns.response(409, 'Amenity already exists')
    def post(self):
        """Create a new amenity"""
        global amenity_counter
        data = request.json
        if 'name' not in data or not data['name'].strip():
            return {'message': 'Amenity name is required and cannot be empty'}, 400

        if any(amenity['name'] == data['name'] for amenity in amenities.values()):
            return {'message': 'Amenity already exists'}, 409

        amenity_id = amenity_counter
        amenities[amenity_id] = {
            'id': amenity_id,
            'name': data['name'],
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow()
        }
        amenity_counter += 1
        return {'message': 'Amenity created successfully'}, 201

@ns.route('/<int:amenity_id>')
@ns.response(404, 'Amenity not found')
class AmenityResource(Resource):
    @ns.doc('get_amenity')
    @ns.marshal_with(amenity_model)
    def get(self, amenity_id):
        """Fetch an amenity given its identifier"""
        amenity = amenities.get(amenity_id)
        if not amenity:
            api.abort(404, "Amenity not found")
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

        amenity = amenities.get(amenity_id)
        if not amenity:
            api.abort(404, "Amenity not found")

        if any(amenity['name'] == data['name'] for id, amenity in amenities.items() if id != amenity_id):
            return {'message': 'Amenity already exists'}, 409

        amenity['name'] = data['name']
        amenity['updated_at'] = datetime.utcnow()
        return {'message': 'Amenity updated successfully'}, 200

    @ns.doc('delete_amenity')
    @ns.response(204, 'Amenity deleted successfully')
    @ns.response(404, 'Amenity not found')
    def delete(self, amenity_id):
        """Delete an amenity given its identifier"""
        if amenity_id not in amenities:
            api.abort(404, "Amenity not found")
        del amenities[amenity_id]
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)
