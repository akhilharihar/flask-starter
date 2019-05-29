import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """
    Default flask instance configuration.
    """
    SECRET_KEY = os.getenv('APP_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig:
    """
    Flask instance configuration in production.
    """
    USE_X_SENDFILE = True


class DevelopmentConfig:
    """
    Flask instance configuration for development.
    """
    pass
