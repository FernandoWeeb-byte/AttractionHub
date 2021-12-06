from flask.app import Flask
import flask_restful as fr
from flask_restful import Api, Resource, reqparse
from ApiGateway import SearchGateway, UserListGateway, LoginGateway, RegisterGateway, SearchDatabase, UserAttraction, MLGateway
from flask_cors import CORS
app = Flask('API_gateway')
CORS(app)
api = Api(app)

api.add_resource(SearchGateway, '/search/')
api.add_resource(UserListGateway, '/manager/')
api.add_resource(LoginGateway, '/login/')
api.add_resource(RegisterGateway, '/register/')
api.add_resource(SearchDatabase, '/data/')
api.add_resource(UserAttraction, '/attraction/')
api.add_resource(MLGateway, '/ml/')

app.run(debug=True)

