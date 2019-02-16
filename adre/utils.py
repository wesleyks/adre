import re
import os
import datetime
from typing import List

FILENAME_NUMBER_REGEX = re.compile(r'^\d{4}')
ROOT = os.path.dirname(os.path.abspath(__file__))


class ADR:
    def __init__(self, filename: str, content: str):
        self.filename = filename
        self.content = content


def list_adr_files(path: str) -> List[str]:
    filenames = os.listdir(path)
    adrs = list(filter(
        lambda fname: filename_extract_number(fname),
        filenames
    ))
    return adrs


def filename_extract_number(filename: str) -> int:
    match = FILENAME_NUMBER_REGEX.match(filename)
    if match:
        return int(match.group(0))
    raise Exception(
        '{filename} doesn\'t appear to be a valid ADR filename'.format(
            filename=filename))


def create_adr(
        title: str, number: int, path: str, status: str = 'Proposed'
) -> str:
    template_path = os.path.join(ROOT, 'adr_template.md')
    title_slug = re.sub(r'[\W_]', '-', title)
    adr_path = os.path.join(
        path,
        '{number:04d}-{title_slug}.md'.format(
            number=number,
            title_slug=title_slug
        )
    )
    template_string = ''
    with open(template_path, 'r') as template_file:
        template_string = template_file.read()

    with open(adr_path, 'w') as output_file:
        output_file.write(template_string.format(
            number=number,
            title=title,
            date=datetime.date.today().isoformat(),
            status=status
        ))
    return adr_path


def extract_adrs(path: str) -> List[ADR]:
    files = list_adr_files(path)
    adrs = []
    for file in files:
        with open(os.path.join(path, file), 'r') as f:
            adrs.append(ADR(file, f.read()))
    return adrs
