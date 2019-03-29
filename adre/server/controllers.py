from typing import Dict

from bottle import view, static_file, Response, request

from adre.utils import extract_adrs
from .settings import STATIC_ROOT


@view('index')
def home() -> Dict:
    return {}


def adrs_list() -> Dict:
    adrs = extract_adrs(request.app.config.adr_path)
    return {
        'adrs': [
            {
                'id': adr.id,
                'title': adr.title,
                'date': adr.date.isoformat(),
                'tags': adr.tags,
                'content': adr.content,
            } for adr in adrs
        ]
    }


def static(filepath: str) -> Response:
    return static_file(filepath, STATIC_ROOT)
