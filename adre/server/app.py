import os

from bottle import Bottle, TEMPLATE_PATH, debug
from bottle import response

from .routes import register_routes
from .settings import APP_ROOT

TEMPLATE_PATH.insert(0, os.path.join(APP_ROOT, 'dist'))


def create_app(adr_path: str) -> Bottle:
    app = Bottle()
    app.config.load_dict({
        'adr_path': adr_path
    })
    register_routes(app)

    @app.hook('after_request')
    def enable_cors() -> None:
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = \
            'PUT, GET, POST, DELETE, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = \
            'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

    debug(True)
    return app
