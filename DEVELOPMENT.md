# Adre Development

## Packaging

Check out https://packaging.python.org/tutorials/packaging-projects/

```bash
# create distributable
python setup.py sdist sdist bdist_wheel

# upload to test
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# upload to prod
twine upload dist/*
```
