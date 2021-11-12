from flask.app import Flask
import flask_restful as fr
from flask_restful import reqparse, Resource
from flask import request, Response

class ApiGateway(Resource):
    def get(self):
        return {
            'data': 'aloalo',
        }, 400

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()
        return args, 200
    def put(self):
        pass
    def delete(self):
        pass