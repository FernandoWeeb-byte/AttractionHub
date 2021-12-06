from flask.app import Flask
import flask_restful as fr
from flask_restful import reqparse, Resource
from flask import request, Response, jsonify, make_response
import requests
import json

URL = 'http://127.0.0.1:8000/'
URLS = 'http://127.0.0.1:6000/'

class SearchGateway(Resource):
    #search for attraction
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title',location="headers", help='Rate cannot be converted')
        parser.add_argument('type',location="headers")
        args = parser.parse_args()
        res = requests.get(URLS + 'list/search/', data=args)
        resp = make_response(res.json(), 200)
        return resp

class SearchDatabase(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id',location="headers")
        args = parser.parse_args()
        res = requests.get(URLS + 'list/attraction/',data=args)
        resp = make_response(res.json(), 200)
        return resp


class UserListGateway(Resource):
    #add attraction to list
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('token')
        parser.add_argument('title')
        parser.add_argument('desc')
        parser.add_argument('urlImg')
        parser.add_argument('rating')
        parser.add_argument('genre', action="append")
        parser.add_argument('stream', action="append")
        parser.add_argument('attractionType')
       
        args = parser.parse_args()
        print(args)
        res = requests.post(URL + 'list/attraction/', data=args)
        resp = make_response(res.json(), 200)
        return resp
        
    #get attraction list of user
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('token', required=True, location='headers')
        parser.add_argument('type', location="headers")
        args = parser.parse_args()
        res = requests.get(URL + 'list/attraction/', data=args)
        resp = make_response(res.json(), 200)
        return resp
        
    #update score, like and status os attraction
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('token', required=True)
        parser.add_argument('title')
        parser.add_argument('score')
        parser.add_argument('like')
        parser.add_argument('status')
        args = parser.parse_args()
        res = requests.put(URL + 'list/attraction/', data=args)
        resp = make_response(res.json(), 200)
        return resp

    #delete attraction from list
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('token', required=True)
        parser.add_argument('title')
        args = parser.parse_args()
        res = requests.delete(URL + 'list/attraction/', data=args)
        resp = make_response(res.json(), 200)
        return resp
        

class RegisterGateway(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('token', location='headers')
        args = parser.parse_args()
        res = requests.get(URL + 'auth/user/', data=args)
        resp = make_response(res.json(), 200)
        return resp

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('username',required=True)
        parser.add_argument('email',required=True)
        parser.add_argument('password',required=True)
        parser.add_argument('attractions')
        args = parser.parse_args()
        res = requests.post(URL + 'auth/register/', data=args)
        resp = make_response(res.json(), 200)
        return resp

    def put(self):
        pass

    def delete(self):
        pass

class LoginGateway(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',required=True)
        parser.add_argument('password',required=True)
        args = parser.parse_args()
        res = requests.post(URL + 'auth/login/', data=args)
        resp = make_response(res.json(), 200)
        return resp

class UserAttraction(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('token', location='headers')
        parser.add_argument('id', location="headers")
        args = parser.parse_args()
        res = requests.get(URL + 'list/database/', data=args)
        resp = make_response(res.json(), 200)
        return resp