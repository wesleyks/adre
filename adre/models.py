import datetime
import re
from typing import List

FILENAME_NUMBER_REGEX = re.compile(r'^\d{4}')
ADR_TITLE_REGEX = re.compile(r'^#\s\d+\.\s(.+)', re.MULTILINE)
ADR_DATE_REGEX = re.compile(r'^date:\s*(.+)', re.MULTILINE | re.IGNORECASE)
ADR_TAG_SECTION_REGEX = re.compile(
    r'#+\s*tags([^#]*)',
    re.DOTALL | re.IGNORECASE
)
ADR_TAG_REGEX = re.compile(r'^\s*([-+*])\s*(.+)', re.MULTILINE | re.IGNORECASE)


class ADR:
    def __init__(self, filename: str, content: str):
        self.filename = filename
        self.content = content

    @property
    def id(self) -> int:
        match = FILENAME_NUMBER_REGEX.match(self.filename)
        if match:
            return int(match.group(0))
        raise Exception(
            '{filename} doesn\'t appear to be a valid ADR filename'.format(
                filename=self.filename))

    @property
    def title(self) -> str:
        match = ADR_TITLE_REGEX.search(self.content)
        if match:
            return match.group(1)
        raise Exception(
            'Could not find title for adr.'
        )

    @property
    def date(self) -> datetime.date:
        match = ADR_DATE_REGEX.search(self.content)
        if match is None:
            raise Exception(
                'Could not find date for adr.'
            )
        return datetime.datetime.strptime(
            match.group(1),
            '%Y-%m-%d'
        ).date()

    @property
    def tags(self) -> List[str]:
        match = ADR_TAG_SECTION_REGEX.search(self.content)
        if match is None:
            return []
        content = match.group(1)
        tags = ADR_TAG_REGEX.findall(content)
        return [tag[1] for tag in tags]
