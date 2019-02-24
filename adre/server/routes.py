from bottle import Bottle

from . import controllers


def register_routes(app: Bottle) -> None:
    app.route('/', ['GET'], controllers.home)
    app.route('/api/adrs', ['GET'], controllers.adrs_list)
    app.route('/static/<filepath:path>', ['GET'], controllers.static)
