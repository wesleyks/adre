import os

from bottle import Bottle, TEMPLATE_PATH, debug

from .routes import register_routes

WEB_ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH.insert(0, os.path.join(WEB_ROOT, 'views'))


def create_app() -> Bottle:
    app = Bottle()
    register_routes(app)
    debug(True)
    return app
