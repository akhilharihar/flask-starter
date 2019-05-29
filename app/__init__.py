import os
from .config import Application, Blueprint
from settings import BaseConfig, ProductionConfig, DevelopmentConfig
from .routes import url_rules


def create_app(test_config=None):
    """
    Flask application factory.

    params:
    config (dict): Custom app configuration.
    """

    app = Application(__name__)
    app.config.from_object(BaseConfig)

    app.config.from_object(BaseConfig)

    if app.config['ENV'] == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    if test_config:
        app.config.from_object(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    _register_extenstions(app)

    app.add_url_rules(url_rules)

    return app


def _register_extenstions(flask_instance):
    """
    Register flask extensions.
    """
    pass


__all__ = ['Blueprint', 'create_app']
