from flask.app import Flask
import flask_restful as fr
from flask_restful import Api, Resource, reqparse
from ApiGateway import SearchGateway, UserListGateway, UserAuthGateway
app = Flask('API_gateway')

api = Api(app)

api.add_resource(SearchGateway, '/search/')
api.add_resource(UserListGateway, '/manager/')
api.add_resource(UserAuthGateway, '/user/')

app.run(debug=True)

