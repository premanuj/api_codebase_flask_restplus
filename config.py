# pylint: disable=too-few-public-methods
import os
import logging
from enum import Enum
from typing import Type
from dotenv import load_dotenv

load_dotenv(verbose=True)


class EnvEnum(Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TESTING = "testing"


class BaseConfig:
    APP_NAME = "Flask Restplus API"
    FLASK_ENV = os.environ.get("FLASK_ENV", EnvEnum.DEVELOPMENT.value)
    HOST = os.environ.get("HOST", "0.0.0.0")
    PORT = int(os.environ.get("PORT", 5000))

    LOG_PATH = os.environ.get("LOG_PATH", "logs/logfile.log")
    DATABASE_URI = os.environ.get("DATABASE_URI")
    if not DATABASE_URI:
        raise Exception('"DATABASE_URI" not set')
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = bool(os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", False))


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    DATABASE_URI = os.environ.get("TEST_DATABASE_URI")
    if not DATABASE_URI:
        raise Exception('"TEST_DATABASE_URI" not set')
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    LOG_LEVEL = logging.DEBUG


class ProductionConfig(BaseConfig):
    DEBUG = True
    LOG_LEVEL = logging.ERROR


def _configuration() -> Type[BaseConfig]:
    env = BaseConfig.FLASK_ENV

    if env == EnvEnum.DEVELOPMENT.value:
        return DevelopmentConfig
    if env == EnvEnum.TESTING.value:
        return TestConfig
    if env == EnvEnum.PRODUCTION.value:
        return ProductionConfig

    raise Exception(f"unknown config type {env}")


Config = _configuration()
