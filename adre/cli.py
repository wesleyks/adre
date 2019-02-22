import os

import click

from adre.utils import (
    filename_extract_number,
    create_adr,
    extract_adrs,
    list_adr_files
)
from adre.server.app import create_app


class ContextObject:
    def __init__(self, path: str):
        self.path = path


@click.group()
@click.pass_context
@click.option(
    '-p', '--path', default='doc/adr/', help='where your adr\'s are stored')
def main(ctx: click.Context, path: str) -> None:
    ctx.obj = ContextObject(
        path=path
    )


@click.command()
@click.pass_obj
def init(ctx_obj: ContextObject) -> None:
    path = ctx_obj.path
    os.makedirs(path, exist_ok=True)
    click.echo('ADR folder initialized in {path}'.format(path=path))


@click.command()
@click.pass_obj
@click.argument('title')
def new(ctx_obj: ContextObject, title: str) -> None:
    """create a new adr with the given title
    """
    path = ctx_obj.path
    filenames = list_adr_files(path)
    adr_numbers = list(map(
        lambda fname: filename_extract_number(fname),
        filenames
    ))
    adr_numbers = sorted(adr_numbers, reverse=True)
    next_number = 1
    if len(adr_numbers):
        next_number = adr_numbers[0] + 1
    adr_path = create_adr(title, next_number, path, 'Proposed')
    click.echo('ADR created: {adr_path}'.format(adr_path=adr_path))


@click.command()
@click.pass_obj
def serve(ctx_obj: ContextObject) -> None:
    adrs = extract_adrs(ctx_obj.path)
    web_app = create_app()
    web_app.run(reloader=True)


main.add_command(init)
main.add_command(new)
main.add_command(serve)
