from flask import Flask
# from api.place_routes_api import place_bp
from api.user_routes_api import user_bp
from api.country_city_routes_api import country_city_bp
from api.amenity_routes_api import amenity_bp

app = Flask(__name__)
# app.register_blueprint(place_bp, url_prefix='/api/v1')
app.register_blueprint(user_bp, url_prefix='/api/v1')
app.register_blueprint(country_city_bp)
app.register_blueprint(amenity_bp)
