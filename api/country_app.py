#!/usr/bin/python3
from flask import Flask, request
from flask_restx import Api, Resource, fields
import datetime

app = Flask(__name__)
api = Api(app, version='1.0', title='Country and City API', description='A simple Country and City API')

ns_country = api.namespace('countries', description='Country operations')
ns_city = api.namespace('cities', description='City operations')

# In-memory data storage
countries = {
    'US': {'name': 'United States', 'code': 'US'},
    'CA': {'name': 'Canada', 'code': 'CA'},
    'FR': {'name': 'France', 'code': 'FR'}
}

cities = []
city_id_counter = 1

# Define models
country_model = api.model('Country', {
    'name': fields.String(required=True, description='The country name'),
    'code': fields.String(required=True, description='The ISO 3166-1 alpha-2 code')
})

city_model = api.model('City', {
    'id': fields.Integer(readOnly=True, description='The city unique identifier'),
    'name': fields.String(required=True, description='The city name'),
    'country_code': fields.String(required=True, description='The country code'),
    'created_at': fields.String(readOnly=True, description='The creation date'),
    'updated_at': fields.String(readOnly=True, description='The last update date')
})

city_create_model = api.model('CityCreate', {
    'name': fields.String(required=True, description='The city name'),
    'country_code': fields.String(required=True, description='The country code')
})

# Country endpoints
@ns_country.route('/')
class CountryList(Resource):
    @ns_country.doc('list_countries')
    @ns_country.marshal_list_with(country_model)
    def get(self):
        """List all countries"""
        return list(countries.values())

@ns_country.route('/<string:country_code>')
@ns_country.response(404, 'Country not found')
@ns_country.param('country_code', 'The country identifier')
class Country(Resource):
    @ns_country.doc('get_country')
    @ns_country.marshal_with(country_model)
    def get(self, country_code):
        """Fetch a country given its identifier"""
        country = countries.get(country_code.upper())
        if country:
            return country
        api.abort(404, "Country not found")

# City endpoints
@ns_city.route('/')
class CityList(Resource):
    @ns_city.doc('list_cities')
    @ns_city.marshal_list_with(city_model)
    def get(self):
        """List all cities"""
        return cities

    @ns_city.doc('create_city')
    @ns_city.expect(city_create_model)
    @ns_city.marshal_with(city_model, code=201)
    def post(self):
        """Create a new city"""
        global city_id_counter
        data = request.json
        country_code = data['country_code'].upper()
        if country_code not in countries:
            api.abort(400, "Invalid country code")

        # Check for unique city name within the same country
        for city in cities:
            if city['name'] == data['name'] and city['country_code'] == country_code:
                api.abort(409, "City name already exists in this country")

        new_city = {
            'id': city_id_counter,
            'name': data['name'],
            'country_code': country_code,
            'created_at': datetime.datetime.utcnow().isoformat(),
            'updated_at': datetime.datetime.utcnow().isoformat()
        }
        cities.append(new_city)
        city_id_counter += 1
        return new_city, 201

@ns_city.route('/<int:city_id>')
@ns_city.response(404, 'City not found')
@ns_city.param('city_id', 'The city identifier')
class City(Resource):
    @ns_city.doc('get_city')
    @ns_city.marshal_with(city_model)
    def get(self, city_id):
        """Fetch a city given its identifier"""
        city = next((city for city in cities if city['id'] == city_id), None)
        if city:
            return city
        api.abort(404, "City not found")

    @ns_city.doc('update_city')
    @ns_city.expect(city_create_model)
    @ns_city.marshal_with(city_model)
    def put(self, city_id):
        """Update a city given its identifier"""
        data = request.json
        city = next((city for city in cities if city['id'] == city_id), None)
        if city:
            country_code = data['country_code'].upper()
            if country_code not in countries:
                api.abort(400, "Invalid country code")

            # Check for unique city name within the same country
            for other_city in cities:
                if other_city['id'] != city_id and other_city['name'] == data['name'] and other_city['country_code'] == country_code:
                    api.abort(409, "City name already exists in this country")

            city.update({
                'name': data['name'],
                'country_code': country_code,
                'updated_at': datetime.datetime.utcnow().isoformat()
            })
            return city
        api.abort(404, "City not found")

    @ns_city.doc('delete_city')
    @ns_city.response(204, 'City deleted')
    def delete(self, city_id):
        """Delete a city given its identifier"""
        global cities
        city = next((city for city in cities if city['id'] == city_id), None)
        if city:
            cities = [c for c in cities if c['id'] != city_id]
            return '', 204
        api.abort(404, "City not found")

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
