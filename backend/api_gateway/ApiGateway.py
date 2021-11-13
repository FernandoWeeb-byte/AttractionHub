from flask.app import Flask
import flask_restful as fr
from flask_restful import reqparse, Resource
from flask import request, Response, jsonify
import requests
import json

URL = 'http://127.0.0.1:8000/'

class ApiGateway(Resource):
    def get(self):
        res = requests.get(URL + 'user/users').json()
        return res, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()
        return args, 200
    def put(self):
        pass
    def delete(self):
        pass