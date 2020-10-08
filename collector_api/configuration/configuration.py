
from collector_api.blueprint import restapi
from collector_api.ext import database

def init_app(app):
    database.init_app(app)
    restapi.init_app(app)