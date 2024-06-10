#!/usr/bin/python3
from flask_restx import abort
from .models import Country, City

def validate_country_code(country_code):
    if not Country.query.filter_by(code=country_code).first():
        abort(400, 'Invalid country code')

def unique_city_name_within_country(city_name, country_code):
    if City.query.filter_by(name=city_name, country_code=country_code).first():
        abort(409, 'City name already exists within the country')
