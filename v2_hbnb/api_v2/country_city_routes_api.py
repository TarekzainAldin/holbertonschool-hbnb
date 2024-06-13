from flask import Blueprint, request, jsonify
from models.city import City
from persistence.city_data_manager import CityDataManager
from persistence.country_data_manager import CountryDataManager

country_city_bp = Blueprint('country_city_bp', __name__)

# Initialize CountryDataManager and load country data
country_data_manager = CountryDataManager()
countries = country_data_manager.get_all()

# Pass the loaded country data to CityDataManager
city_data_manager = CityDataManager(countries=countries)

@country_city_bp.route('/countries', methods=['GET'])
def get_countries():
    return jsonify([country.to_dict() for country in countries]), 200

@country_city_bp.route('/countries/<string:country_code>', methods=['GET'])
def get_country(country_code):
    country = country_data_manager.get(country_code)
    if country is None:
        return jsonify({'error': 'Country not found'}), 404
    return jsonify(country.to_dict()), 200

@country_city_bp.route('/countries/<string:country_code>/cities', methods=['GET'])
def get_cities_by_country(country_code):
    cities = city_data_manager.get_by_country(country_code)
    return jsonify([city.to_dict() for city in cities]), 200

@country_city_bp.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    required_fields = ['name', 'country_code']
    if not data or not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing data'}), 400
    city = City(**data)
    result = city_data_manager.save(city)
    return jsonify(result), 201

@country_city_bp.route('/cities', methods=['GET'])
def get_cities():
    cities = city_data_manager.get_all()
    return jsonify([city.to_dict() for city in cities]), 200

@country_city_bp.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    city = city_data_manager.get(city_id)
    if city is None:
        return jsonify({'error': 'City not found'}), 404
    return jsonify(city.to_dict()), 200

@country_city_bp.route('/cities/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    city = city_data_manager.get(city_id)
    if city is None:
        return jsonify({'error': 'City not found'}), 404

    data = request.get_json()
    for key, value in data.items():
        setattr(city, key, value)
    city_data_manager.update(city)
    return jsonify(city.to_dict()), 200

@country_city_bp.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = city_data_manager.get(city_id)
    if city is None:
        return jsonify({'error': 'City not found'}), 404

    city_data_manager.delete(city_id)
    return '', 204
