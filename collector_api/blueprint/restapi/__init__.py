from flask import Blueprint
from flask_restful import Api
from .collector_resources import CollectFTPResource

bp = Blueprint("restapi", __name__, url_prefix="/api")
api = Api(bp)

api.add_resource(CollectFTPResource, "/collector/")

def init_app(app):
    app.register_blueprint(bp)