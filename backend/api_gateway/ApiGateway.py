from flask.app import Flask
import flask_restful as fr
from flask_restful import reqparse
from flask import request, Response
import requests

class ApiGateway(fr.Resource):
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
        return 
    def delete(self):
        return