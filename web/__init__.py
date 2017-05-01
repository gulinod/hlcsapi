from flask import Flask
from flask_restful import Resource, Api
import json

# import the API classes
from web.manage.api import BasicColor


# Initialize flask
app = Flask(__name__)
api = Api(app, prefix='/api/v1')

# Add API routes
api.add_resource(BasicColor, '/basic-color')


def run(debug=False):
    # run the app
    app.run( debug=debug, port=5003, host='0.0.0.0')
