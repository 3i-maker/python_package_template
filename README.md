# Project

License: MIT

## Deploy Package

- add gitlab keys to ~/.pypirc   


- python setup.py sdist bdist_wheel 


- python -m twine upload --repository gitlab dist/*