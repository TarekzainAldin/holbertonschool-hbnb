from flask import Blueprint, jsonify
from persistence.storage import Storage

storage = Storage()
countries_bp = Blueprint('countries_bp', __name__)

@countries_bp.route('/countries', methods=['GET'])
def get_countries():
    return jsonify(storage.get_countries()), 200

@countries_bp.route('/countries/<string:country_code>', methods=['GET'])
def get_country(country_code):
    country = storage.get_country(country_code)
    if country:
        return jsonify(country), 200
    else:
        return jsonify({"error": "Country not found"}), 404

@countries_bp.route('/countries/<string:country_code>/cities', methods=['GET'])
def get_cities_by_country(country_code):
    country = storage.get_country(country_code)
    if not country:
        return jsonify({"error": "Country not found"}), 404
    
    cities = [city for city in storage.get_cities() if city.country_code == country_code]
    return jsonify(cities), 200
