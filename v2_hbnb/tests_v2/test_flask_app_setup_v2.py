# tests/test_flask_app_setup.py

import unittest
from flask import Flask
from api.app import app, country_city_bp

class TestFlaskAppSetup(unittest.TestCase):

    def test_blueprint_registration(self):
        # Check if country_city_bp blueprint is registered
        self.assertIn(country_city_bp, app.blueprints.values())

if __name__ == '__main__':
    unittest.main()
