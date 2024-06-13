from flask import Blueprint, jsonify, request
from persistence.city_data_manager import CityDataManager

city_bp = Blueprint('city_bp', __name__)
city_manager = CityDataManager()

@city_bp.route('/cities', methods=['GET'])
def get_cities():
    cities = city_manager.get_all()
    return jsonify([city.to_dict() for city in cities]), 200

@city_bp.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    city = city_manager.get(city_id)
    if city:
        return jsonify(city.to_dict()), 200
    else:
        return jsonify({"error": "City not found"}), 404

@city_bp.route('/cities', methods=['POST'])
def create_city():
    data = request.json
    if 'name' not in data or 'country_code' not in data:
        return jsonify({"error": "Name and country_code are required"}), 400

    new_city = city_manager.create(data['name'], data['country_code'])
    if new_city:
        return jsonify(new_city.to_dict()), 201
    else:
        return jsonify({"error": "Invalid country code"}), 400

@city_bp.route('/cities/<int:city_id>', methods=['PUT'])
def update_city(city_id):
    data = request.json
    if 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    updated_city = city_manager.update(city_id, data['name'])
    if updated_city:
        return jsonify(updated_city.to_dict()), 200
    else:
        return jsonify({"error": "City not found"}), 404

@city_bp.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    deleted = city_manager.delete(city_id)
    if deleted:
        return '', 204
    else:
        return jsonify({"error": "City not found"}), 404
