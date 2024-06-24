from flask import Blueprint, request, jsonify
from model.city import City
from persistence.storage import Storage

storage = Storage()
cities_bp = Blueprint('cities_bp', __name__)

@cities_bp.route('/cities', methods=['POST'])
def create_city():
    data = request.json
    if 'name' not in data or 'country_code' not in data:
        return jsonify({"error": "Missing name or country_code"}), 400

    country = storage.get_country(data['country_code'])
    if not country:
        return jsonify({"error": "Invalid country_code"}), 400

    if any(city.name == data['name'] and city.country_code == data['country_code'] for city in storage.get_cities()):
        return jsonify({"error": "City name must be unique within the same country"}), 409

    city = City(name=data['name'], country_code=data['country_code'])
    return jsonify({"id": city.id, "name": city.name, "country_code": city.country_code, "created_at": city.created_at, "updated_at": city.updated_at}), 201

@cities_bp.route('/cities', methods=['GET'])
def get_cities():
    return jsonify([vars(city) for city in storage.get_cities()]), 200

@cities_bp.route('/cities/<string:city_id>', methods=['GET'])
def get_city(city_id):
    city = storage.get_city(city_id)
    if city:
        return jsonify(vars(city)), 200
    else:
        return jsonify({"error": "City not found"}), 404

@cities_bp.route('/cities/<string:city_id>', methods=['PUT'])
def update_city(city_id):
    city = storage.get_city(city_id)
    if not city:
        return jsonify({"error": "City not found"}), 404

    data = request.json
    if 'name' in data:
        city.name = data['name']
    if 'country_code' in data:
        country = storage.get_country(data['country_code'])
        if not country:
            return jsonify({"error": "Invalid country_code"}), 400
        city.country_code = data['country_code']
    
    city.update_city()
    return jsonify(vars(city)), 200

@cities_bp.route('/cities/<string:city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = storage.get_city(city_id)
    if not city:
        return jsonify({"error": "City not found"}), 404

    city.delete_city()
    return '', 204
