from setuptools import setup

setup(
    name='adre',
    version='0.0',
    description='ADR Extended',
    packages=['adre'],
    install_requires=[
        'click',
        'bottle'
    ],
    entry_points={
        'console_scripts': [
            'adre=adre.cli:main'
        ]
    }
)
