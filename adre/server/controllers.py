from typing import Dict

from bottle import view, static_file, Response


@view('home')
def home() -> Dict:
    return {}


def static(filepath: str) -> Response:
    return static_file(filepath)
