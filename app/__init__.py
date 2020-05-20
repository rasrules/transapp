"""App Main

Declaration of App Factory pattern
This will make the app endpoints available, load plugins and
configurations
"""
import logging
import sys
import os
#import yaml
from flask import Flask, g, current_app
from config.config import Config
from flask_mongoengine import MongoEngine
#from flask_cors import CORS
from app.custome_response import MyResponse
# pylint: disable=invalid-name, import-outside-toplevel


# Extensions
db = MongoEngine()



def create_app(config_class=Config):
    """Initialize the core application.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.response_class = MyResponse

    db.init_app(app)

    # Logging setup
    handler = logging.FileHandler('debug.log')
    handler.setLevel("DEBUG")
    formatter = logging.Formatter(
        fmt='%(asctime)s %(levelname)-8s %(module)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    handler.setFormatter(formatter)

    loggers = [
        app.logger, logging.getLogger('main')
    ]
    for logger in loggers:
        formatter = logging.Formatter(
            fmt='%(asctime)s %(levelname)-8s %(name)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler = logging.FileHandler('debug.log')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    print(str(app.config["ENVIRONMENT"]))
    if app.config["ENVIRONMENT"] != "DEVELOPMENT":
        logging.disable(logging.WARNING)

    with app.app_context():

        from app.main import bp as main_bp, routes
        app.register_blueprint(main_bp, url_prefix='/main')

        return app
