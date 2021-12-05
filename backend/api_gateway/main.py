from flask.app import Flask
import flask_restful as fr
from flask_restful import Api, Resource, reqparse
from ApiGateway import SearchGateway, UserListGateway, LoginGateway, RegisterGateway, SearchDatabase
from flask_cors import CORS
app = Flask('API_gateway')
CORS(app)
api = Api(app)

api.add_resource(SearchGateway, '/search/')
api.add_resource(UserListGateway, '/manager/')
api.add_resource(LoginGateway, '/login/')
api.add_resource(RegisterGateway, '/register/')
api.add_resource(SearchDatabase, '/data/')

app.run(debug=True)

