#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
import uuid
from datetime import datetime

app = Flask(__name__)
api = Api(app, version='1.0', title='User Management API',
          description='A simple User Management API')
