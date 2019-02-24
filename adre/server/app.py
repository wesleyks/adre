import os

from bottle import Bottle, TEMPLATE_PATH, debug

from .routes import register_routes

WEB_ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH.insert(0, os.path.join(WEB_ROOT, 'views'))


def create_app(adr_path: str) -> Bottle:
    app = Bottle()
    app.config.load_dict({
        'adr_path': adr_path
    })
    register_routes(app)
    debug(True)
    return app
