from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='adre',
    version='0.0.1',
    description='ADR Extended',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'click',
        'bottle'
    ],
    entry_points={
        'console_scripts': [
            'adre=adre.cli:main'
        ]
    },
    include_package_data=True,
)
