#!/usr/bin/env python3
import random
import string

from flask import Flask, request
from flask_restful import Resource, Api

application = Flask(__name__)
api = Api(application)


class Ansokan(Resource):
    def get(self):
        return {'namn': '', 'alder': '', 'franDatum': '', 'tomDatum': '', 'orsak': []}, 200

    def post(self):
        ansokan = request.get_json()
        return {'ansokan': ansokan, 'signatur': ''.join(random.choices(string.ascii_uppercase + string.digits, k=512))}, 201

api.add_resource(Ansokan, '/ansokan')

if __name__ == '__main__':
   application.run()
