from flask.app import Flask
import flask_restful as fr
from flask_restful import reqparse, Api
from ApiGateway import ApiGateway
app = Flask('API_gateway')

api = Api(app)

api.add_resource(ApiGateway, '/api_gateway')

app.run()

