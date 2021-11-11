from flask.app import Flask
import flask_restful as fr
from flask_restful import reqparse
import ApiGateway
app = Flask('API_gateway')

api = fr.Api(app)

api.add_resource(ApiGateway, '/api_gateway')

app.run(threaded=True)

