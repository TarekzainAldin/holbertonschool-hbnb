# api/amenity_routes_api.py
from datetime import datetime
from flask import Blueprint, request, jsonify
from models.amenity import Amenity
from persistence.amenity_data_manager import AmenityDataManager

amenity_bp = Blueprint('amenity_bp', __name__)
amenity_data_manager = AmenityDataManager()

@amenity_bp.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Missing name field'}), 400

    name = data['name']
    if amenity_data_manager.exists(name):
        return jsonify({'error': 'Amenity with this name already exists'}), 409

    amenity = Amenity(name=name)
    result = amenity_data_manager.save(amenity)
    return jsonify(result), 201

@amenity_bp.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = amenity_data_manager.get_all()
    return jsonify([amenity.to_dict() for amenity in amenities]), 200

@amenity_bp.route('/amenities/<int:amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = amenity_data_manager.get(amenity_id)
    if amenity is None:
        return jsonify({'error': 'Amenity not found'}), 404
    return jsonify(amenity.to_dict()), 200

@amenity_bp.route('/amenities/<int:amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    amenity = amenity_data_manager.get(amenity_id)
    if amenity is None:
        return jsonify({'error': 'Amenity not found'}), 404

    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Missing name field'}), 400

    name = data['name']
    if amenity_data_manager.exists(name) and amenity_data_manager.get_by_name(name).id != amenity_id:
        return jsonify({'error': 'Amenity with this name already exists'}), 409

    amenity.name = name
    amenity.updated_at = datetime.now()
    amenity_data_manager.update(amenity)
    return jsonify(amenity.to_dict()), 200

@amenity_bp.route('/amenities/<int:amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    amenity = amenity_data_manager.get(amenity_id)
    if amenity is None:
        return jsonify({'error': 'Amenity not found'}), 404

    amenity_data_manager.delete(amenity_id)
    return '', 204
