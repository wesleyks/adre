from typing import Dict

from bottle import view, static_file, Response, request

from adre.utils import extract_adrs


@view('home')
def home() -> Dict:
    return {}


def adrs_list() -> Dict:
    adrs = extract_adrs(request.app.config.adr_path)
    return {
        'data': [
            {
                'id': adr.id,
                'title': adr.title,
                'date': adr.date.isoformat(),
            } for adr in adrs
        ]
    }


def static(filepath: str) -> Response:
    return static_file(filepath)
