#!/usr/bin/python3
import uuid
from flask import request
from flask_restx import Namespace, Resource, fields, reqparse, inputs, abort
from persistence.review_repository import ReviewRepository
from persistence.place_data_manager import PlaceDataManager
from models.review import Review
from datetime import datetime

# Initialize namespaces
ns_reviews = Namespace('reviews', description='Operations related to reviews')
ns_users = Namespace('users', description='Operations related to users')
ns_places = Namespace('places', description='Operations related to places')

# Repositories
review_repository = ReviewRepository()
place_repository = PlaceDataManager()

# Model for review creation and update
review_model = ns_reviews.model('Review', {
    'user_id': fields.Integer(required=True, description='User ID'),
    'rating': fields.Integer(required=True, description='Rating (1-5)'),
    'comment': fields.String(description='Comment')
})

# Request parser for place_id and review_id
parser = reqparse.RequestParser()
parser.add_argument('place_id', type=int, help='Place ID', location='path')
parser.add_argument('review_id', type=str, help='Review ID', location='path')

@ns_reviews.route('/<int:place_id>/reviews')
class PlaceReviews(Resource):
    @ns_reviews.expect(review_model)
    @ns_reviews.response(201, 'Review created successfully')
    @ns_reviews.response(400, 'Invalid request')
    @ns_reviews.response(404, 'Place not found')
    def post(self, place_id):
        """Create a new review for a specified place."""
        args = parser.parse_args()
        user_id = args['user_id']
        rating = args['rating']
        comment = args.get('comment', '')

        # Validate place_id exists
        place = place_repository.get(place_id)
        if not place:
            return {'message': 'Place not found'}, 404

        # Validate user_id and ensure user is not the host of the place
        if user_id == place.host_id:
            return {'message': 'Host cannot review their own place'}, 400

        # Validate rating within range 1-5
        if not (1 <= rating <= 5):
            return {'message': 'Rating must be between 1 and 5'}, 400

        # Create new review
        review_id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()
        new_review_data = {
            'id': review_id,
            'user_id': user_id,
            'place_id': place_id,
            'rating': rating,
            'comment': comment,
            'created_at': created_at,
            'updated_at': updated_at
        }
        review_repository.save(new_review_data)

        return {'message': 'Review created successfully', 'review_id': review_id}, 201

    @ns_reviews.marshal_list_with(review_model)
    @ns_reviews.response(200, 'Success')
    @ns_reviews.response(404, 'Place not found')
    def get(self, place_id):
        """Retrieve all reviews for a specific place."""
        place = place_repository.get(place_id)
        if not place:
            return {'message': 'Place not found'}, 404

        reviews = review_repository.get_reviews_by_place(place_id)
        return reviews, 200

@ns_users.route('/<int:user_id>/reviews')
class UserReviews(Resource):
    @ns_reviews.marshal_with(review_model)
    @ns_reviews.response(200, 'Success')
    @ns_reviews.response(404, 'User not found')
    def get(self, user_id):
        """Retrieve all reviews written by a specific user."""
        reviews = review_repository.get_reviews_by_user(user_id)
        if not reviews:
            return {'message': 'User not found'}, 404
        return reviews, 200

@ns_reviews.route('/<string:review_id>')
class ReviewResource(Resource):
    @ns_reviews.marshal_with(review_model)
    @ns_reviews.response(200, 'Success')
    @ns_reviews.response(404, 'Review not found')
    def get(self, review_id):
        """Retrieve detailed information about a specific review."""
        review = review_repository.get(review_id)
        if not review:
            return {'message': 'Review not found'}, 404
        return review, 200

    @ns_reviews.expect(review_model)
    @ns_reviews.response(204, 'Review updated successfully')
    @ns_reviews.response(400, 'Invalid request')
    @ns_reviews.response(404, 'Review not found')
    def put(self, review_id):
        """Update an existing review."""
        new_review_data = request.json
        new_review_data['id'] = review_id
        new_review_data['updated_at'] = datetime.now()

        # Validate rating within range 1-5
        if 'rating' in new_review_data and not (1 <= new_review_data['rating'] <= 5):
            return {'message': 'Rating must be between 1 and 5'}, 400

        if review_repository.update(review_id, new_review_data):
            return '', 204
        else:
            return {'message': 'Review not found'}, 404

    @ns_reviews.response(204, 'Review deleted successfully')
    @ns_reviews.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a specific review."""
        if review_repository.delete(review_id):
            return '', 204
        else:
            return {'message': 'Review not found'}, 404
