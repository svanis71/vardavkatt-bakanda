#!/usr/bin/env python3
import random
import string

from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

application = Flask(__name__)
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'
api = Api(application)


class Ansokan(Resource):
    def get(self):
        return {'namn': '', 'alder': '', 'franDatum': '', 'tomDatum': '', 'orsak': []}, 200

    def post(self):
        print('POST!!')
        print(request)
        ansokan = request.get_json()
        print(ansokan['namn'])
        return {'ansokan': {'namn': 'smilla'}, 'signatur': ''.join(random.choices(string.ascii_uppercase + string.digits, k=512))}, 201

api.add_resource(Ansokan, '/ansokan')

if __name__ == '__main__':
   application.run()
