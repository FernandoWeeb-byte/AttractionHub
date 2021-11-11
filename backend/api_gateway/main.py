from flask.app import Flask
import flask_restful as fr
from flask_restful import reqparse
app = Flask('API_gateway')

api = fr.Api(app)

class Api_Gateway(fr.Resource):
    def get(self):
        return {
            'data': 'aloalo',
        }, 400

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()
        return args, 200

api.add_resource(Api_Gateway, '/api_gateway')

app.run()

