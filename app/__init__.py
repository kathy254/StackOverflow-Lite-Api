from flask import Flask

from instance.config import app_config
from .api.v1.views.user_views import auth

def create_app(config):
    '''function creating the flask app'''
    app = Flask(__name__)
    app.register_blueprint(auth)
    app.config.from_object(app_config[config])
    return app