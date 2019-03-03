# pylint: disable=redefined-outer-name,unused-variable

import logging
from time import time

from flask_migrate import Migrate
from flask import Flask, g, request, make_response, abort
from logzero import logger, loglevel, logfile, formatter
from config import Config
from api.utils.json_encoder import JsonEncoder
from api.resources.api import api
from api.models.meta import db


def _init_logging(app: Flask):
    log = logging.getLogger("werkzeug")
    log.disabled = True
    loglevel(app.config.get("LOG_LEVEL"))
    formatter(logging.Formatter("[%(asctime)s] - %(levelname)s: %(message)s"))

    if app.config.get("FLASK_ENV") != "testing":
        logfile(
            app.config.get("LOG_PATH"),
            maxBytes=10_000_000,
            backupCount=3,
            loglevel=app.config.get("LOG_LEVEL"),
        )


def _register_before_request(app: Flask):
    def before_request():
        """
            A function to run before each request
        """

        logger.debug(f"Request [{request.method}] : {request.base_url}")
        g.start_time = time()

    app.before_request(before_request)


def _register_after_request(app: Flask):
    def after_request(response):
        """
            A function to run after each request.
        """

        execution_time = time() - g.start_time
        logger.debug(f"Request completion time: {execution_time}")

        return response

    app.after_request(after_request)


def config_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    return app


def create_app() -> Flask:
    app = config_app()

    app.json_encoder = JsonEncoder
    api.init_app(app)
    db.init_app(app)
    Migrate(app, db)

    _init_logging(app)
    _register_before_request(app)
    _register_after_request(app)

    return app
