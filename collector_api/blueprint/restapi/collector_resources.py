from flask import jsonify, abort
from flask_restful import Resource
from collector_api.controller import abstract_controller

class CollectFTPResource(Resource):
    def get(self):
        abstract_controller.get_all('an_cardeter')
        return jsonify({
            'teste': 1
        })
    
    def post(self):
        return jsonify({
            'teste': 2
        })

    def delete(self):
        return jsonify({
            'teste': 3
        })

    def put(self):
        return jsonify({
            'teste': 4
        })